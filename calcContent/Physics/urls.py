from django.urls import path
from . import views

urlpatterns = [
    # URL paths
    path('physics/', views.physicsMain, name='physics'),
    path('equations_of_motion/', views.equations_of_motion, name='equations_of_motion'),
    path('proj_motion/', views.proj_motion, name='proj_motion'),
    
    # API paths
    path('equations_of_motion_api/', views.equations_of_motion_api, name='equations_of_motion_api')
]
