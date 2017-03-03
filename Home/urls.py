from django.conf.urls import url
from . import views

urlpatterns = [
    #   /all users test/
    url(r'^$', views.channels, name='index'),
    url(r'^channels/(?P<channel_id>[0-9]+)/$', views.channelDetail, name='channel_details'),
    url(r'^users/(?P<user_id>[0-9]+)/$', views.userDetail, name='user_details'),
    url(r'^login/$', views.loginView, name='login'),
    url(r'^createChannel/$', views.createChannel, name='createChannel'),
    url(r'logout/$', views.logOut, name= 'logout'),
    url(r'about/$', views.about, name='about'),

]
