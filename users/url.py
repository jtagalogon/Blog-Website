from django.conf.urls import url
from users import views

urlpatterns = [
	#url(r'^details/(?P<id>/d+>)/$', views.details, name='details'),
	url(r'^$', views.index, name='index'),
];