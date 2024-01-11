from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render 

def homepage(request):
        contents = {"title":"Home"}
        return render(request, 'index.html', contents)

def login(request):
        return render(request, 'login.html')

def aboutUs(request):
        return render (request, 'about_us.html')
