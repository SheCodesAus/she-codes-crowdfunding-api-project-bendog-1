from django.urls import path 
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view(), name="project-list"),
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name="project-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
