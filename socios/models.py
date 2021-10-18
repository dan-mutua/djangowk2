from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse







class Post(models.Model):
  
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  caption = models.CharField(max_length=200)
  comment = models.TextField(blank=True)
  posttime=models.DateTimeField(auto_now_add=True)
  likes = models.IntegerField(default=0)



def __str__(self):
    return self.name + " | " + str(self.author)
    
  


