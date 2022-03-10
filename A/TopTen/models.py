from typing import MappingView
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class TOP(models.Model):
    Title = models.CharField(max_length=200)
    body = models.TextField()   
    Name_dirctor = models.CharField(max_length=100,blank=True)
    Imdb_number = models.FloatField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    images = models.ImageField()
    
    def __str__(self):
        return self.Title
    




