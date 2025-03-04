from django.urls import path
from . import views

urlpatterns = [
    #URL Paths
    path('chemistry/', views.chemistryMain, name='chemistry'),
    path('gaseous/', views.gaseous, name='gaseous'),
    path('chem-thermo/', views.chem_thermo, name='chem-thermo'),

    #API Paths
    path('gaseous_api/', views.gaseous_api, name='gaseous_api'),
    path('kinetic_theory_api/', views.kineticTheory_api, name='kinetic_theory_api'),
    path('rms_velocity_api/', views.rms_velocity_api, name='rms_velocity_api'),
    path('internal-energy/', views.internal_energy, name='internal-energy'),   
]
