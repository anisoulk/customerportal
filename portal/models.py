from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Area(models.Model):
	#A topic the user is learning about
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User)

	def __str__(self):
		return self.text

class Network(models.Model):
	#Network in the specific Area
	area = models.ForeignKey(Area)
	text = models.TextField()
	status = models.TextField()
	ip_switch = models.TextField()
	ip_ping = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	#class Meta:
	#	verbose_name_plural = 'entries'

	def __str__(self):
		return self.text[:50] + "..."