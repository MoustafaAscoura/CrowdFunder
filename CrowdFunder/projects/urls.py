from django.urls import path

from projects.views import project_detail, project_list , create_project

urlpatterns = [
    path('projects/', project_list, name='project_list'),
    path('projects/<int:id>/', project_detail, name='project_detail'),
    path('projects/create', create_project, name='project_create'),
]
