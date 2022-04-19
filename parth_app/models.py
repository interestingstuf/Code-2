import email
from email import message
from pyexpat import model
from django.db import models
from numpy import maximum

class contactform1(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.EmailField()
    contact=models.CharField(max_length=15)
    message=models.CharField(max_length=200)
    
