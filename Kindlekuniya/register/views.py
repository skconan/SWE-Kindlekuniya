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



def home(request):
    return render(request, 'home.html')
