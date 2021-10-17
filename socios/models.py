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
  id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
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

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like')

	def user_liked_post(sender, instance, *args, **kwargs):
   like = instance
	  post = like.post
	  sender = like.user
	  notify = Notification(post=post, sender=sender, user=post.user, notification_type=1)
	  notify.save()

def user_unlike_post(sender, instance, *args, **kwargs):
	   like = instance 
	post = like.post
	sender = like.user

	notify = Notification.objects.filter(post=post, sender=sender, notification_type=1)
	notify.delete()