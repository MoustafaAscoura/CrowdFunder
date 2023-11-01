from django.urls import path
from django.contrib.auth.decorators import login_required
from projects.views import project_detail, project_list, CreateProject,EditProjectView,delete, CategoryView, TagView , donate,feature

urlpatterns = [
    path('', project_list, name='project_list'),
    path('<int:pk>/', project_detail, name='project_detail'),
    path('<int:pk>/delete', delete, name='project_delete'),
    path('create', CreateProject.as_view(), name='project_create'),
    path('<int:pk>/edit/', EditProjectView.as_view(), name='edit_project'),
    path('category/<str:category>' , CategoryView.as_view() , name='category'),
    path('tags/<str:tag>' , TagView.as_view() , name='tag'),
    path('<int:pk>/donate',donate , name='donate'),
    path('<int:pk>/feature',feature , name='feature'),
    
]
