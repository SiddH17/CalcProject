from django.urls import path
from . import views

urlpatterns = [
    # URL paths
    path('physics/', views.physicsMain, name='physics'),
    path('equations_of_motion/', views.equations_of_motion, name='equations_of_motion'),
    path('proj_motion/', views.proj_motion, name='proj_motion'),
    path('electrostatics/', views.electrostatics, name='electrostatics'),
    path('thermodynamics/',views.thermodynamics, name='thermodynamics'),
    path('rayoptics/', views.rayOptics, name='rayoptics'),
    path('current-electricity/', views.currentElectricity, name='current-electricity'),
    path('modern-physics/', views.modern_physics, name='modern-physics'),
    path('emi/', views.emi, name='emi'),
    path('wave-optics/', views.wave_optics, name='wave-optics'),
    
    # API paths
    path('equations_of_motion_api/', views.equations_of_motion_api, name='equations_of_motion_api'),
    path('proj_motion_api/',views.proj_motion_api, name='proj_motion_api'),
    path('electrostatics_api/', views.electrostatics_api, name='electrostatics_api'),
    path('mirror_api/', views.mirror_api, name='mirror_api'),
    path('lens_api/', views.lens_api, name='lens_api'),
    path('ohms-law-api/', views.ohms_law_api, name='ohms-law-api'),
    path('power-api/', views.power_api, name='power-api'),
    path('resistivity-api/', views.resistivity_api, name='resistivity-api'),
    path('heat-and-energy-api/', views.heat_and_energy_api, name='heat-and-energy-api'),
    path('equipartition-of-energy/', views.equipartition_of_energy, name='equipartition-of-energy'),
    path('de-broglie-wavelength/', views.debroglie_wavelength, name='de-broglie-wavelength'),
    path('ev-to-joule-conversion/', views.ev_joule_conversion, name='ev-to-joule-conversion'),
    path('bohr-model/', views.bohr_model, name='bohr-model'),
    path('be-md/', views.be_md, name='be-md'),
    path('inductance/', views.inductance_api, name='inductance'),
    path('wavelength-frequency/', views.wavelength_frequency, name='wavelength-frequency'),
    path('rydberg-formula/', views.rydberg_formula, name='rydberg-formula'),
]
