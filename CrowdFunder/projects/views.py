from django.http import HttpResponse
from django.shortcuts import render ,get_object_or_404,redirect
from . models import Project, Photo , Donation
from . forms import ProjectFileForm
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.core.exceptions import PermissionDenied



def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, id=pk)
    return render(request, 'projects/project_detail.html', {'project': project})

@login_required
def delete(request, pk):
    project = get_object_or_404(Project, id=pk)
    
    if project.user != request.user:
        return HttpResponse("You are not authorized to delete this project.")
    if project:
        project.delete()
        return redirect('project_list')
    else:
        return HttpResponse("Sorry, project not found")   
    
@login_required
def donate(request , pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        print(request.POST['donate'])
        # donation = Donation
        # donation.amount = request.POST['donate']
        # donation.project = id
        # donation.user = request.user
        donation = Donation.objects.create(amount=request.POST['donate'] , user=request.user , project=project)


    return render(request, 'projects/project_detail.html', {'project': project})


class CreateProject(generic.CreateView):
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
    

def similar(request):

   pass