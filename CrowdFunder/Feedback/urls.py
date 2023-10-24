from django.urls import path
from .views import *

urlpatterns = [
    path('<int:id>/report', report_project, name='report'),
    path('<int:id>/review', report_project, name='create_review'),
    path('<int:id>/comment', report_project, name='create_comment'),
]