from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField




class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
 
  images =  CloudinaryField( 'image', null=True, )
  caption = models.CharField(max_length=200)
  posttime=models.DateTimeField(auto_now_add=True)
  likes = models.ManyToManyField(User, related_name='blogp',default=0)


  def total_likes(self):
    return self.likes.count()

  def __str__(self):
      return self.name + " | " + str(self.author)

  def get_absolute_url(self):
    return reverse('postdetail', args=(str(self.id)))    



class Comment(models.Model):
  post =models.ForeignKe(Post, related_name="comments", on_delete=models.CASCADE)   
  name = models.CharField(max_length=200) 
  body = models.TextField()
  date_added = models.DateTimeField(auto_now_add=True)

  def  __str__(self):
    return '%s - %s' % (self.post.title, self.name)
    
  


