from django.urls import path

from projects.views import project_detail, project_list , create_project,edit_project,delete,category_list,category_detail,create_category

urlpatterns = [
    path('projects/', project_list, name='project_list'),
    path('projects/<int:id>/', project_detail, name='project_detail'),
    path('projects/delete/<int:id>/', delete, name='project_delete'),
    path('projects/create', create_project, name='project_create'),
    path('projects/edit/<int:id>', edit_project, name='edit_project'),
    path('category/' , category_list , name='category.list'),
    path('category/<str:category>/' , category_detail , name='category_detail'),
    path('category/create' , create_category , name='category_create'),
]
