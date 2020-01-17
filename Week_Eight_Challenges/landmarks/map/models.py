from django.conf import settings
from django.db import models

class Landmark(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.name} located at {self.address}"
