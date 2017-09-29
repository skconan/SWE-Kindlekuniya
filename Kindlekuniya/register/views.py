from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.db import connection
from .forms import signupForm, signinForm
from .models import signupModelForm,User

def signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            form = signupModelForm(request.POST)        
            form.save()
            return render(request, "signup.html")
    else:
        form = signupForm()
    return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = signinForm(request.POST)
        if form.is_valid() and User.objects.filter(email=request.POST['email']).filter(password=request.POST['password']):
            return render(request, "home.html")
    else:
        form = signinForm()
    return render(request, 'signin.html', {'form': form})


def home(request):
    return render(request, 'home.html')
