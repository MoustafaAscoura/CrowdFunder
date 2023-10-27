from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/report', ReportProject.as_view(), name='report'),
    path('<int:pk>/review', report_project, name='create_review'),
    path('<int:pk>/comment', create_comment, name='create_comment'),
    path('reports', report_list, name='report_list')
]