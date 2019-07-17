from django.conf.urls import url
from django.urls import path
from posts import views

urlpatterns = [
	path('', views.index, name='view')
	
];