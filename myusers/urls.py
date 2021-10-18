from django.urls import path


urlpatterns = [
     path('', Homev.as_view(),name='home'),
     path('post/<int:pk>', PostD.as_view(),name='postdetail'),
     path('add_post/',AddP.as_view(),name='add-post'),
]