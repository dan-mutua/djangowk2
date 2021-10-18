from django.urls import path
from socios import views
from . import views
from .views import Homev,PostD


urlpatterns = [
     path('', Homev.as_view(),name='home'),
     path('post/<int:pk>', PostD.as_view(),name='postdetail')
]