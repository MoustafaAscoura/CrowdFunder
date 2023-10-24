from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from projects.models import Project

def index(request):
    projects = Project.objects.all()
    print(projects)
    return render(request, 'home/home.html', {'projects': projects})

def contact(request):
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

class SearchView(generic.ListView):
    template_name = 'projects/project_list.html'
    model = Project
    context_object_name = 'projects'

    def get_queryset(self):
        param = self.request.GET.get('param')
        projects = Project.objects.filter(title__icontains=param)
        self.extra_context={'search':param}
        return projects
