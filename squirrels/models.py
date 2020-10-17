from django.db import models

class Sighting(models.Model):
    UniqueSquirrelID = models.CharField(max_length=100)
    Date=models.CharField(max_length=100)
