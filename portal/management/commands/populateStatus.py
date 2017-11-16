from django.core.management.base import BaseCommand, CommandError
from portal.models import Area, Network

#import paramiko, socket

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'Custom Command to populate the Status of the Networks'

    def add_arguments(self, parser):
        parser.add_argument('area_id', nargs='+', type=int)

    def handle(self, *args, **options):
    	area = Area.objects.get(id=options['area_id'])
    	networks = area.network_set.order_by('-date_added')
    	port=22
    	IP='192.168.201.37'
    	username='admin'
    	password='clk430'
    	cmd='ping 192.168.89.2'
    	ssh=paramiko.SSHClient()
    	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    	for network in networks:
            try:
            	ssh.connect(IP,port,username,password, timeout=5)
            	stdin,stdout,stderr=ssh.exec_command(cmd)
            	outlines=stdout.readlines()
            	pingline = outlines[-2]
            	pingline_words = pingline.split()
            	pingline_percent = pingline_words[5]
                #poll = Poll.objects.get(pk=poll_id)
            except socket.timeout:
            	pingline_percent = 'N\\A'
            sh.close()
            if pingline_percent == '0%':
            	network.status = 'green'
            elif pingline_percent == 'N\\A':
            	network.status = 'gray'
            else:
            	network.status = 'red'   