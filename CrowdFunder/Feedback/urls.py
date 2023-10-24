from django.urls import path
from .views import *

urlpatterns = [
    path('<int:id>/report', ReportProject.as_view(), name='report'),
    path('<int:id>/review', report_project, name='create_review'),
    path('<int:id>/comment', report_project, name='create_comment'),
    path('reports', report_list, name='report_list')
]