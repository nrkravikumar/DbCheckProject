from django.shortcuts import render,redirect
from SampleApp .models import *

# Create your views here.

def home(request):
	d = RegisterPage.objects.all()
	return render(request,'home.html',{"g":d})

def logn(request):
	return render(request,'login.html')

def register(request):
	if request.method == "POST":
		a = request.POST.get('f')
		b = request.POST.get('l')
		c = request.POST.get('e')
		d = request.POST.get('p')
		u = request.POST.get('u')
		pw = request.POST.get('pw')
		y = RegisterPage(fname=a,lname=b,mail=c,phone=d,user=u,pwd=pw)
		y.save()
		return redirect('/')
	return render(request,'register.html')
