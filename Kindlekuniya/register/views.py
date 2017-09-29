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
        email = request.POST['email']
        password = request.POST['password']
        isMatch = User.objects.filter(email=email).filter(password=password)
        if form.is_valid() and isMatch:
            user = User.objects.get(email=email)
            context = {'user':user}
            return render(request, "profile.html",context)
    else:
        form = signinForm()
    return render(request, 'signin.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')
