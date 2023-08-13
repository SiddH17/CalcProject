from django.urls import path
from . import views

app_name = 'Mathematics'

urlpatterns = [
    path('mathematics/', views.mathematicsMain, name='mathematics'),    
]
