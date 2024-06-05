from django.urls import path
from . import views

urlpatterns = [
    path('mathematics/', views.mathematicsMain, name='mathematics'),
    path('trigonometry/', views.trigonometry, name='trigonometry'),
    path('parabola/', views.parabola, name='parabola'),    
    path('ellipse/', views.ellipse, name='ellipse'),
    path('hyperbola/', views.hyperbola, name='hyperbola'),
    path('statistics/', views.statistics, name='statistics'),

    # APIs
    path('trigonometry_api/', views.trigonometry_api, name='trigonometry_api'),
    path('ellipse_api/', views.ellipse_api, name='ellipse_api'),
    path('hyperbola_api/', views.hyperbola_api, name='hyperbola_api'),
]
