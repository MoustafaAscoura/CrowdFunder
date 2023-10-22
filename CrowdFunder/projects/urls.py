from django.urls import path

from projects.views import project_detail, project_list , create_project ,category_list, create_category

urlpatterns = [
    path('', project_list, name='project_list'),
    path('<int:id>/', project_detail, name='project_detail'),
    path('create-project', create_project, name='project_create'),
    path('category' , category_list , name='category.list'),
    path('create-category' , create_category , name='category.create'),
]
