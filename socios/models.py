from django.db import models
from django.contrib.auth.models import User
import uuid
from django.urls import reverse




def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

# Create your models here.
class Postm(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='content_owner')
file = models.FileField(upload_to=user_directory_path)


class Post(models.Model):
  
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  caption = models.CharField(max_length=200)
  comment = models.TextField(blank=True)
  content = models.ManyToManyField(Postm,  related_name='contents')
  posttime=models.DateTimeField(auto_now_add=True)
  likes = models.IntegerField(default=0)



def __str__(self):
    return self.name + " | " + str(self.author)
    
  
def get_absolute_url(self):
		return reverse('postdetails', args=[str(self.id)])

def __str__(self):
		return str(self.id)  

