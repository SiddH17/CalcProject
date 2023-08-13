from django.urls import path
from . import views

urlpatterns = [
    path('physics/', views.physicsMain, name='physics'),
    path('equations_of_motion/', views.equations_of_motion, name='equations_of_motion'),
    path('proj_motion/', views.proj_motion, name='proj_motion'),
    
]
