from django.urls import path
from . import views

urlpatterns = [
    path('mathematics/', views.mathematicsMain, name='mathematics'),
    path('trigonometry/', views.trigonometry, name='trigonometry'),
    path('parabola/', views.parabola, name='parabola'),    
    path('ellipse/', views.ellipse, name='ellipse'),
    path('hyperbola/', views.hyperbola, name='hyperbola'),
    path('stats/', views.stats, name='stats'),
    path('quadratics', views.quadratics, name='quadratics'),

    # APIs
    path('trigonometry_api/', views.trigonometry_api, name='trigonometry_api'),
    path('ellipse_api/', views.ellipse_api, name='ellipse_api'),
    path('hyperbola_api/', views.hyperbola_api, name='hyperbola_api'),
    path('statistics_api/', views.statistics_api, name='statistics_api'),
    path('quadratics_api/', views.quadratics_api, name='quadratics_api'),
    path('spread_api', views.spread_api, name='spread_api'),
]
