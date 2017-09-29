from django import forms
from django.forms import ModelForm

class signupForm(forms.Form):
    email = forms.EmailField(required=True,max_length=128)
    firstName = forms.CharField(required=True,max_length=128)
    lastName = forms.CharField(required=True,max_length=128)
    password = forms.CharField(required=True,max_length=128, widget=forms.PasswordInput)
    confirmPassword = forms.CharField(required=True,max_length=128, widget=forms.PasswordInput)
    phoneNO = forms.IntegerField(required=True)

class signinForm(forms.Form):
    email = forms.EmailField(required=True,max_length=128)
    password = forms.CharField(required=True,max_length=128, widget=forms.PasswordInput)    