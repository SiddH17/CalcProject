from django.urls import path
from . import views

urlpatterns = [
    #URL Paths
    path('chemistry/', views.chemistryMain, name='chemistry'),
    path('gaseous/', views.gaseous, name='gaseous'),
    path('chem-thermo/', views.chem_thermo, name='chem-thermo'),
    path('mole-concept/', views.mole_concept, name='mole-concept'),
    path('atomic-structure/', views.atomic_structure, name='atomic-structure'),

    #API Paths
    path('gaseous_api/', views.gaseous_api, name='gaseous_api'),
    path('kinetic_theory_api/', views.kineticTheory_api, name='kinetic_theory_api'),
    path('rms_velocity_api/', views.rms_velocity_api, name='rms_velocity_api'),
    path('internal-energy/', views.internal_energy, name='internal-energy'),   
    path('ideal-gas-mole/', views.ideal_gas_equation_mole, name='ideal-gas-mole'),
    path('hydrogen-structure-api/', views.hydrogen_structure_api, name='hydrogen-structure-api'),
]
