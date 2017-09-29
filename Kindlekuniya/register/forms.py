from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    firstName = forms.CharField(max_length=30, required=False, help_text='Optional.')
    lastName = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    phoneNO = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ( 'username','firstName', 'lastName', 'email','phoneNO', 'password1', 'password2', )