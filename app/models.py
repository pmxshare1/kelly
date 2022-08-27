from pyexpat import model
from django.db import models

# Create your models here.
class HomePage(models.Model):
    name = models.CharField(max_length=100)
    skill = models.CharField(max_length=200)

class AboutPage(models.Model):
    header = models.TextField()
    website = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    age = models.IntegerField()
    qual = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    freelance = models.BooleanField(default=False)
    img = models.ImageField(upload_to='media/', default='media/default.jpg')