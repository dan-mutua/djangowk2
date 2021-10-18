from django import forms
from .models import Post



class  PostF(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('author','name','caption','comment')

    widgets={
      'author':forms.TextInput(attrs={'class':'form-control'}),
      'name':forms.TextInput(attrs={'class':'form-control'}),
      'caption':forms.TextInput(attrs={'class':'form-control'}),
      'comment':forms.TextInput(attrs={'class':'form-control'}),
    }