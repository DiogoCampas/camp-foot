from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    club = models.CharField(max_length=200)
    
    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
    



class Publication(models.Model):
    title = models.CharField(max_length=5000)
    content = models.TextField()
    author = models.ForeignKey(Record, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title









    
    







