from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views


app_name = 'webapp'

urlpatterns = [
    #url('', views.index, name='index'),
    #url('', views.base, name='base'),
    #url('', views.login, name='login'),
    #url('', views.signup, name='signup'),
    #url('', views.home, name='home'),

    url(r'^login/', views.login, name='login'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^home/', views.home, name='home'),
    url(r'^delete/', views.delete, name='delete'),
    url('^post/', views.post_page),
    path('', views.blog_page),
];

