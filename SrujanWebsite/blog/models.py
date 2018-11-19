from django.db import models

# Create your models here.

class Title(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=250)
