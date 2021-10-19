from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView
from .models import Post
from .forms import PostF
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy

# Create your views here.




class Homev(ListView):
  model = Post
  template_name='home.html'

class PostD(DetailView):
  model = Post
  template_name='post-detail.html'  

class AddP(CreateView):
  model = Post
  form_class= PostF
  template_name='upload.html'

  success_url= reverse_lazy('home')
  # fields= '__all__'

def LikeView(request,pk):
  post = get_object_or_404(Post,id=request.POST.get('post_id'))
  post.likes.add(request.user)
  return HttpResponseRedirect(reverse('home', args=[str(pk=pk)]))  


def get_context_data(self, *args, **kwargs):
  cat_menu =Category.objects.all()
  context = super(AddP,self).get_context_data(**kwargs)
  stuff= get_object_or_404(Post, id=self.kwargs['pk'])
  total_likes=stuff.total_likes()
  context["cat_menu"]= cat_menu
  context["total_likes"]= total_likes
  return context

