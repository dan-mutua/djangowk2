from django import forms
from .models import Post



class  PostF(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('author','images','caption')

    widgets={
      
      'caption':forms.TextInput(attrs={'class':'form-control'}),
      
    }