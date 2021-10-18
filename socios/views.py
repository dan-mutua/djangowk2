from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post

# Create your views here.
class  Homev(ListView):
  model = Post
  template_name='home.html'

class PostD(DetailView):
  model = Post
  template_name='post-detail.html'  