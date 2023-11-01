from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Avg
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from projects.models import Project
from django.db.models import Q

def index(request):    
    allprojects = list(Project.objects.all())
    featured=filter(lambda x:x.is_featured,allprojects)
    top_rated_projects = sorted(allprojects, key=lambda x:x.rate, reverse=True)[:6]
    latest_projects = sorted(allprojects, key=lambda x:x.created_at, reverse=True)[:6]
    featured_projects = sorted(featured, key=lambda x:float(x.rate * 20) + x.percentage, reverse=True)[:6]

    return render(request, 'home/home.html', {'top_rated_projects': top_rated_projects,
                                              'latest_projects': latest_projects, 'featured_projects':featured_projects})

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
        projects = Project.objects.filter(
            Q(title__icontains=param) | Q(tags__icontains=param)
        )
        self.extra_context = {'search': param}
        return projects