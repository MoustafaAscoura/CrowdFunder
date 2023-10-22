from django.urls import path

from projects.views import project_detail, project_list , create_project,edit_project,delete,category_list,category_detail,create_category

urlpatterns = [
    path('', project_list, name='project_list'),
    path('<int:id>', project_detail, name='project_detail'),
    path('delete/<int:id>', delete, name='project_delete'),
    path('create', create_project, name='project_create'),
    path('edit/<int:id>', edit_project, name='edit_project'),
    path('category/' , category_list , name='category.list'),
    path('category/<str:category>' , category_detail , name='category_detail'),
    path('category/create' , create_category , name='category_create'),
]
