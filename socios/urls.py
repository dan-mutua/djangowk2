from django.urls import path
from socios import views
from . import views
from .views import Homev,PostD,AddP,LikeView


urlpatterns = [
     path('', Homev.as_view(),name='home'),
     path('post/<int:pk>', PostD.as_view(),name='postdetail'),
     path('add_post/',AddP.as_view(),name='add-post'),
     path('like/<int:pk>',LikeView, name='like_post'),
]