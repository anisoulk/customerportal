from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(request):
	#Log the user out 
	logout(request)
	return HttpResponseRedirect(reverse('portal:index'))

def register(request):
	#Register a New User
	if request.method != 'POST':
		form = UserCreationForm()
	else:
		form = UserCreationForm(data=request.POST)
		if form.is_valid():
			new_user = form.save()
			#Log the User in and Redirect to HomePage
			authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
			login(request, authenticated_user)
			return HttpResponseRedirect(reverse('portal:index'))
	context = {'form': form}
	return render(request, 'users/register.html', context)

