from os import name
from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class Career(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads', blank=False)
    hiring = models.CharField(max_length=30)
    video = models.CharField(max_length=999, blank=True)
    date= models.DateField()

    def __str__(self):
        return self.fname