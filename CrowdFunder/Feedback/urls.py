from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/report', ReportProject.as_view(), name='report'),
    path('<int:pk>/review', create_review, name='create_review'),
    path('<int:pk>/comment', create_comment, name='create_comment'),
    path('reports', report_list, name='report_list'),
    path('<int:pk>/comment/<int:comment_id>/report', report_comment, name='report_comment')

    # path('reports/<int:pk>', create_report, name='create')
]