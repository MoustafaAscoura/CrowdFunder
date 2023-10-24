from django.urls import path
from .views import *

urlpatterns = [
    path('report/<int:id>', report_project, name='report')
]