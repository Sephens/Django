from pyexpat import model
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    User = get_user_model()
    Title = models.CharField(max_length=200)
    Text = models.TextField
    Author = models.ForeignKey
    Created_date = models.DateTimeField
    Published_date = models.DateTimeField
    
