from django.urls import path
from . import views

urlpatterns = [
    path('equations_of_motion/', views.equations_of_motion, name='equations_of_motion'),

]
