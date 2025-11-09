from django.db import models

# Create your models here.
#Model for users in the system
class Reg_Users(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
