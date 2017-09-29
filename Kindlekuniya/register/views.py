from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import userProfile
from django.db import connection
from .forms import userProfileForm, userSigninForm
from .models import userProfileModel,userProfile

def signup(request):
    if request.method == 'POST':
        form = userProfileForm(request.POST)
        if form.is_valid():
            form = userProfileModel(request.POST)        
            form.save()

            return render(request, "signup.html")

    else:
        form = userProfileForm()
    return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = userSigninForm(request.POST)
        if form.is_valid() and userProfile.objects.filter(email=request.POST['email']).filter(password=request.POST['password']):
            return render(request, "home.html")
    else:
        form = userSigninForm()
    return render(request, 'signin.html', {'form': form})


def home(request):
    return render(request, 'home.html')
