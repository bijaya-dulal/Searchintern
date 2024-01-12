from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render 
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
                contents = {"title": "Login", 'error': error}
                return render(request, "login.html", contents)

            return render(request, "login.html", contents)
        else:
            print("Inside else")
            contents = {"title": "Login", 'error': error}
            return render(request, "login.html", contents)

    except Exception as e:
        print("Error:", str(e))  # Print or log the exception message
        contents = {"title": "Login", 'error': error, 'exception_message': str(e)}
        return render(request, "login.html", contents)



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
            name = request.POST.get('name')
            email = request.POST.get('email')
            pw = request.POST.get('pass')
            vpw = request.POST.get('v-pass')
            print("Email:", email)
            print("Password:", pw)
            if is_valid_email(email):
               print("in valid email")
               if is_valid_password(pw):
                   print("in valid pass")
                   if is_valid_name(name):
                       print("in valid name")
                       return HttpResponse("welcome")
                   else:
                        contents = {'title': "signup",
                                   'error':True,
                                   'error_message':"invalid name",
                                   }
                        return render(request, "signup.html", contents)
               else:
                   
                   contents = {'title': "signup",
                                   'error':True,
                                   'error_message':"invalid password",
            
                                } 
                   return render(request, "signup.html", contents)
            else:    
                             
                 contents = {'title': "signup",
                                   'error':True,
                                   'error_message':"invalid email",
                                   }
                 return render(request, "signup.html", contents)
        else:
            contents={"title":"signup",
                      'error':False}
            print("Inside else")
            return render(request, "signup.html", contents)

    except Exception as e:
        print("Error:", str(e))

    


#rex match function
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    match = re.match(pattern, email)
    return bool(match)
def is_valid_password(password):
    # At least 8 characters, containing both letters and numbers
    pattern = r'^(?=.*[a-zA-Z])(?=.*\d).{8,}$'

   
    match = re.match(pattern, password)

    # Return True if the password is valid, False otherwise
    return bool(match)


def is_valid_name(name):
    # Define the regex pattern for name validation
    # Allows letters and optional spaces
    pattern = r'^[a-zA-Z]*$'


    # Use re.match to check if the name matches the pattern
    match = re.match(pattern, name)

    # Return True if the name is valid, False otherwise
    return bool(match)