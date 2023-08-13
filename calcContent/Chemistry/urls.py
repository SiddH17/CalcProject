from django.urls import path
from . import views

app_name = 'Chemistry'

urlpatterns = [
    path('chemistry/', views.chemistryMain, name='chemistry'),
]
