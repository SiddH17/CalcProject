from django.urls import path
from . import views

urlpatterns = [
    # URL paths
    path('physics/', views.physicsMain, name='physics'),
    path('equations_of_motion/', views.equations_of_motion, name='equations_of_motion'),
    path('proj_motion/', views.proj_motion, name='proj_motion'),
    path('electrostatics/', views.electrostatics, name='electrostatics'),
    path('thermodynamics/',views.thermodynamics, name='thermodynamics'),
    
    # API paths
    path('equations_of_motion_api/', views.equations_of_motion_api, name='equations_of_motion_api'),
    path('proj_motion_api/',views.proj_motion_api, name='proj_motion_api'),
    path('electrostatics_api/', views.electrostatics_api, name='electrostatics_api'),
]
