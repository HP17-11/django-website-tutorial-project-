from django.urls import path
from . import views

urlpatterns = [
    
    path('projects/',views.projects, name="projects"),
    path('project/<str:n>/',views.project, name="project"),

    path('create-project/',views.createproject, name='create-project'),
    path('update-project/<str:n>/', views.updateproject, name='update-project'),
    path('delete-project/<str:n>/', views.deleteproject, name='delete-project'),


]
