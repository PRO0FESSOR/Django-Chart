from django.db import models

# Create your models here.x

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    bio = models.CharField(max_length=100)
    age = models.IntegerField()
