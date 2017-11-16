import paramiko, socket
from django.shortcuts import render
from .models import Area, Network

from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.management import call_command



#import paramiko, socket

# Create your views here.

def index(request):
	# The non-logged in HomePage View Function for Portal App
	return render(request, 'portal/index.html')

@login_required
def home(request):
	# The logged-in HomePage View Function for Portal App
	areas = Area.objects.filter(owner=request.user).order_by('date_added')
	#for area in areas:
	#for area in areas:
	#	call_command('populateStatus', area.id)
	#context = {'areas': areas, 'area': area, 'networks': networks}
	return render(request, 'portal/home.html')

@login_required
def areas(request):
	# The Areas View Function
	areas = Area.objects.filter(owner=request.user).order_by('date_added')
	context = {'areas': areas}
	return render(request, 'portal/areas.html', context)

@login_required
def area(request, area_id):
	#The Specific Area View Function
	area = Area.objects.get(id=area_id)
	#Make Sure the Area belong to the Specific logged in Customer
	if area.owner != request.user:
		raise Http404
	networks = area.network_set.order_by('-date_added')
	port=22
	#IP='192.168.201.37'
	username='admin'
	#cmd='ping 192.168.89.2'    	
	ssh=paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	for network in networks:
		try:
			IP = network.ip_switch
			if IP == '192.168.200.35' or IP == '192.168.200.34':
				cmd = 'ping ' + network.ip_ping + ' count 5'
			else:
				cmd = 'ping ' + network.ip_ping
			word = network.text
			lastletters = word[7]+word[8]
			if lastletters == '80':
				password = 'mdaoptix'
			else:
				password = 'clk430'
			ssh.connect(IP,port,username,password, timeout=5)
			stdin,stdout,stderr=ssh.exec_command(cmd)
			outlines=stdout.readlines()
			pingline = outlines[-2]
			pingline_words = pingline.split()
			if IP == '192.168.200.35' or IP == '192.168.200.34':
				pingline_percent = pingline_words[6]
			else:
				pingline_percent = pingline_words[5]
		except socket.timeout:
			pingline_percent = 'N\\A'
		ssh.close()
		if pingline_percent == '0%':
			network.status = 'green'
		elif pingline_percent == 'N\\A':
			network.status = 'gray'
		else:
			network.status = 'red'
	context = {'area': area, 'networks': networks}
	return render(request, 'portal/area.html', context)

