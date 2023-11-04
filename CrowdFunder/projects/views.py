from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseNotFound
from django.shortcuts import render ,get_object_or_404,redirect
from . models import Project, Photo , Donation
from . forms import ProjectFileForm
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from operator import or_
from functools import reduce


def project_list(request):
    projects = Project.objects.all()
    
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, id=pk)
    print(project.is_featured)
    # This query checks for any project within the same category or have a common tag
    # similars = Project.objects.filter(category=project.category).exclude(id=pk)[:4]
    similars = Project.objects.filter(reduce(or_, [Q(tags__icontains=tag) for tag in project.tags_array]
                                        + [Q(category=project.category)])).exclude(id=pk)[:4]
    return render(request, 'projects/project_detail.html', {'project': project, 'similars': similars})

@login_required
def delete(request, pk):
    project = get_object_or_404(Project, id=pk)
    
    if project.user != request.user:
        return HttpResponse("You are not authorized to delete this project.")
    if project:
        project.delete()
        return redirect('project_list')
    else:
        return HttpResponseNotFound("Sorry, project not found")   
    
@login_required
def donate(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        if float(request.POST['donate']) > 0:
            donation = Donation.objects.create(amount=request.POST['donate'] , user=request.user , project=project)
        else:
            HttpResponseBadRequest("Donation Amount is invalid")

    return redirect(reverse_lazy('project_detail', kwargs={'pk': pk}))

@login_required
def feature(request, pk):
    project = get_object_or_404(Project, id=pk)
    if request.user.is_superuser:
        project.is_featured = not project.is_featured
        project.save()
    return redirect(reverse_lazy('project_list'))


class CreateProject(LoginRequiredMixin, generic.CreateView):
    model = Project
    form_class = ProjectFileForm
    success_url = reverse_lazy('project_list')
    template_name='projects/project_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        
        files = self.request.FILES.getlist('file')
        if files:
            for f in files:
                Photo.objects.create(project=self.object,photo=f)

        return super().form_valid(form)
    
# @login_required
# def create_project(request):
#     if request.method == 'POST':
#         form = ProjectFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             project = form.save(commit=False)
#             project.user = request.user
#             project.save()

#             files = request.FILES.getlist('file')
#             for f in files:
#                 Photo.objects.create(project=project, photo=f)

#             return redirect('project_list')
#     else:
#         form = ProjectFileForm()

#     return render(request, 'projects/project_form.html', {'form': form})
    

class EditProjectView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectFileForm
    template_name='projects/project_form.html'
    success_url = reverse_lazy('project_list')


    def form_valid(self, form):       
        files = self.request.FILES.getlist('file')
        if files:
            for f in files:
                Photo.objects.create(project=self.object,photo=f)

        return super().form_valid(form)
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        self.extra_context={'edit':True}
        if obj.user != self.request.user:
            raise PermissionDenied("You are not authorized to edit this project.")
        return obj
    
# @login_required
# def edit_project(request, pk):
#     project = get_object_or_404(Project, pk=pk)
#     if project.user != request.user:
#         raise PermissionDenied("You are not authorized to edit this project.")

#     if request.method == 'POST':
#         form = ProjectFileForm(request.POST, request.FILES, instance=project)
#         if form.is_valid():
#             form.save()

#             files = request.FILES.getlist('file')
#             for f in files:
#                 Photo.objects.create(project=project, photo=f)

#             return redirect('project_list')
#     else:
#         form = ProjectFileForm(instance=project)

#     return render(request, 'projects/project_form.html', {'form': form, 'edit': True})    

class CategoryView(generic.ListView):
    template_name = 'projects/project_list.html'
    model = Project
    context_object_name = 'projects'
    def get_queryset(self):
        name = self.kwargs.get('category')
        projects = self.model.objects.filter(category=name)
        self.extra_context={'category':name}
        return projects

class TagView(generic.ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    def get_queryset(self):
        tag = self.kwargs.get('tag')
        projects = Project.objects.filter(tags__icontains=tag)
        self.extra_context={'tag':tag}
        return projects
    