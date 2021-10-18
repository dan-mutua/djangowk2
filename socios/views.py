from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Post
from .forms import PostF

# Create your views here.
class  Homev(ListView):
  model = Post
  template_name='home.html'

class PostD(DetailView):
  model = Post
  template_name='post-detail.html'  

class AddP(CreateView):
  model = Post
  form_class= PostF
  template_name='upload.html'
  # fields= '__all__'
