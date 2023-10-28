from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/report', ReportProject.as_view(), name='report'),
    path('<int:pk>/review', create_review, name='create_review'),
    path('<int:pk>/comment', create_comment, name='create_comment'),
    path('reports', Reports.as_view(), name='report_list'),
    path('<int:pk>/report/<int:comment_id>', report_comment, name='report_comment'),
    path('<int:comment_id>/reply/', create_reply, name='create_reply'),
]