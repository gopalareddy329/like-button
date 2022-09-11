from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    email=models.EmailField(max_length=200)
    REQUIRED_FIELDS=[]
    
    def __str__(self):
        return self.username
    
class Artical(models.Model):
    name=models.CharField(max_length=200)
    likes=models.ManyToManyField(User,related_name="likes",blank=True)
    
    def total_likes(self):
        return self.likes.count()
    def __str__(self):
        return self.name