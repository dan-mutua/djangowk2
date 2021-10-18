from django.urls import path
from socios import views
from . import views
from .views import Homev


urlpatterns = [
     path('', Homev.as_view(),name='home'),
]