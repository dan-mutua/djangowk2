from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms

class SignupForm(UserCreationForm):
  email = forms.EmailField(widget=forms.EmailInput)
  first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
  last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
 

  class Meta:
    model = User
    fields= ('username','firstname', 'last_name','email', 'password1','password2')

    def __init__(self,*args,**kwargs):
      super(SignupForm, self).__init__(*args,**kwargs)

      self.fields['username'].widget.attrs['class':'form-control']
      self.fields['password1'].widget.attrs['class':'form-control']
      self.fields['password2'].widget.attrs['class':'form-control']


class EditProfile(UserChangeForm):
  email = forms.EmailField(widget=forms.EmailInput)
  first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
  last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
 

  class Meta:
    model = User
    fields= ('username','firstname', 'last_name','email', 'password')      