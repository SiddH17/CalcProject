from django.urls import path
from . import views

urlpatterns = [
    path('register_api/', views.register_api, name='register_api'),
]
