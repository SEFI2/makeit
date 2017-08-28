from django.conf.urls import url, include
from django.contrib import admin
from . import views



urlpatterns = [
    url(r'^signup/$', views.SignUp.as_view() , name='sign_up'),
    url(r'^login/$', views.Login , name='login'),
    url(r'^logout/$', views.Logout , name='logout'),
    url(r'^$' , views.AllUsers.as_view(), name='all_users'),
    url(r'^(?P<pk>[0-9]+)/$', views.ShowProfile.as_view(), name='show_profile'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.UpdateProfile, name='update_profile')
]
