from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from signup.models import Rider,Driver
from login.models import Otp
from django.template.context_processors import csrf
from django.views import generic
from django.contrib.auth.decorators import login_required
from passlib.hash import oracle10
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib import auth
from django.contrib.sessions.models import Session
from django.utils.crypto import get_random_string
import smtplib

def home(request):
	return render(request,'home.html')

def select1(request):
	return render(request,'select1.html')

def riderlogin(request):
	return render(request,'loginrider.html')

def driverlogin(request):
	return render(request,'logindriver.html')

def authriderinfo(request):
	uname = request.POST.get('uname', '')
	password = request.POST.get('pass', '')
	user = auth.authenticate(username=uname, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/rider/rhome/')
	else:
		messages.add_message(request,messages.WARNING,'Incorrect Username or password')
		return render(request,'loginrider.html')

def authdriverinfo(request):
	uname = request.POST.get('uname', '')
	password = request.POST.get('pass', '')
	user = auth.authenticate(username=uname, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/driver/dhome/')
	else:
		messages.add_message(request,messages.WARNING,'Incorrect Username or password')
		return render(request,'logindriver.html')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/home/home/')



