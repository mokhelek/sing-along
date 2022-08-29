from email import message
from django.db import models

# Create your models here.

class Contact(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    #headline = models.CharField(max_length=200)
    message = models.TextField()
