from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render 

def homepage(request):
        contents = {"title":"Home"}
        return render(request, 'index.html', contents)

def login(request):
        contents = {"title":"Login"}
        return render(request, 'login.html', contents)

def aboutUs(request):
        contents = {"title":"aboutus"}
        return render (request, 'about_us.html', contents)

def register(request):
    contents = {"title":"Registration"}
    return render(request,"register_form.html",contents)

def userprofile(request):
    contents = {"title":"profile"}
    return render(request,"user_profile.html",contents)

def signup(request):
      contents = {'title':"signup"}
      return render(request,"sign_up.html",contents)