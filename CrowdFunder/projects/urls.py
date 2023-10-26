from django.urls import path
from django.contrib.auth.decorators import login_required
from projects.views import project_detail, project_list, CreateProject,EditProjectView,delete, CategoryView, TagView , donate

urlpatterns = [
    path('', project_list, name='project_list'),
    path('<int:id>/', project_detail, name='project_detail'),
    path('<int:id>/delete', delete, name='project_delete'),
    path('create', login_required(CreateProject.as_view()), name='project_create'),
    path('<int:pk>/edit/', EditProjectView.as_view(), name='edit_project'),
    path('category/<str:category>' , CategoryView.as_view() , name='category'),
    path('tags/<str:tag>' , TagView.as_view() , name='tag'),
    path('<int:id>/donate',EditProjectView.as_view() , name='donate'),
    path('<int:id>/donate-test',donate,name='project_donate'),
]
