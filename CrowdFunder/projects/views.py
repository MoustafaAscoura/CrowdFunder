from django.http import HttpResponse
from django.shortcuts import render ,get_object_or_404,redirect
from . models import Project
from . forms import ProjectForm
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'projects/project_detail.html', {'project': project})

@login_required
def delete(request, id):
    project = get_object_or_404(Project, id=id)
    
    if project.user != request.user:
        return HttpResponse("You are not authorized to delete this project.")
    if project:
        project.delete()
        # print(request.user,'I am delete function in views.py')
        return redirect('project_list')
    else:
        return HttpResponse("Sorry, project not found")   

class CreateProject(generic.CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('project_list')
    template_name='projects/create/create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

@login_required
def edit_project(request, id):
    project = get_object_or_404(Project, id=id)
    
    # Check if the current user is the owner of the gun
    if project.user != request.user:
        return HttpResponse("You are not authorized to edit this project.")

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project.title = form.cleaned_data['title']
            project.details = form.cleaned_data['details']
            project.total_target = form.cleaned_data['total_target']
            project.start_time = form.cleaned_data['start_time']
            project.end_time = form.cleaned_data['end_time']
            project.category = form.cleaned_data['category']

            # Check if a new image is provided
            # if 'image' in request.FILES:
            #     project.image = form.cleaned_data['image']
            project.save()
            return redirect('project_list')
    else:
        form = ProjectForm({
            'title': project.title,
            'details': project.details,
            'total_target': project.total_target,
            'start_time': project.start_time,
            'end_time': project.end_time,
            'category': project.category,
            }
        )

    context = {
        'form': form
    }
    return render(request, 'projects/create/edit.html', context)

class CategoryView(generic.ListView):
    template_name = 'projects/project_list.html'
    model = Project
    context_object_name = 'projects'
    def get_queryset(self):
        name = self.kwargs.get('category')
        projects = self.model.objects.filter(category=name)
        print(name,projects)
        self.extra_context={'category':name}
        return projects

class TagView(generic.ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    def get_queryset(self):
        tag = self.kwargs.get('tag')
        projects = Project.objects.filter(tags__contains=[tag])
        print(tag,projects)
        self.extra_context={'tag':tag}
        return projects