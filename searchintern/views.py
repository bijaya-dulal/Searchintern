from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render 
import hashlib
import re


def hash_password(password):
    password_bytes = password.encode('utf-8')
    sha256_hash = hashlib.sha256()
    sha256_hash.update(password_bytes)
    return sha256_hash.hexdigest()

def check_password(entered_password, stored_hashed_password):
    hashed_entered_password = hash_password(entered_password)
    return hashed_entered_password == stored_hashed_password
#----------------------------------------------
def homepage(request):
        contents = {"title":"Home"}
        return render(request, 'index.html', contents)

def login(request):
        contents = {"title":"Login",
                    'error':True }
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
    print("signup")
    error = False
    
    try:
        if request.method == 'POST':
            print("Inside POST method")
            # Accessing form data
            email = request.POST.get('email')
            pw = request.POST.get('pass')
            print("Email:", email)
            print("Password:", pw)
            if is_valid_email(email):
                pass
            else:
                 error = True
            # return render(request, "signup.html", contents)
            return render(request, "index.html")
        else:
            print("Inside else")
            return render(request, "signup.html", contents)

    except Exception as e:
        print("Error:", str(e))

    


#rex match function
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    match = re.match(pattern, email)
    return bool(match)