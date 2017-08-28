from django.conf.urls import url, include
from django.contrib import admin
from . import views



urlpatterns = [
    url(r'^create/', views.CreateBlog , name='create_blog'),
    url(r'^update/(?P<pk>[0-9]+)', views.EditBlog , name='edit_blog'),
    url(r'^(?P<pk>[0-9]+)/$', views.BlogLook.as_view(), name='blog_look'),
    url(r'^$', views.AllBlogs.as_view(), name='all_blogs'),
    url(r'^activities/(?P<article_type>[^/]+)/(?P<activity_type>[^/]+)/(?P<pk>[0-9]+)/$' , views.Activities , name='activity')
]

