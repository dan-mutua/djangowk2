from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  caption = models.CharField(max_length=200)
  comment = models.TextField(blank=True)

  def __str__(self):
    return self.name + " | " + str(self.author)

