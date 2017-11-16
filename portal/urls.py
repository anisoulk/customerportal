#"""Defines URL patterns for portal."""

from django.conf.urls import url
from . import views

urlpatterns = [
	#non logged HomePage
	url(r'^$', views.index, name='index'),
	#logged HomePage
	url(r'^home/$', views.home, name='home'),
	#Show All Areas View Page
	url(r'^areas/$', views.areas, name='areas'),
	#Show the Specific Area Networks Pages
	url(r'^areas/(?P<area_id>\d+)/$', views.area, name='area'),
]