from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import userProfile

def signup(req):
    if(req.method == 'POST'):
        firstName = req.POST['firstName']
        lastName = req.POST['lastName']
        email = req.POST['email']
        password = req.POST['password']
        phoneNO = req.POST['phoneNO']
        user_Profile = userProfile(email=email,firstName=firstName,lastName=lastName,password=password,phoneNO=phoneNO)
        user_Profile.save()
        return render(req,"signup.html")
    else:
        return render(req,"signup.html")

def home(request):
    return render(request,'home.html')