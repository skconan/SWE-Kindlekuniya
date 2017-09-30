from django import forms
from django.forms import ModelForm
from django.core.validators import RegexValidator


class signupForm(forms.Form):
    email = forms.EmailField(required=True, max_length=128)
    firstName = forms.CharField(required=True, max_length=128)
    lastName = forms.CharField(required=True, max_length=128)
    password = forms.CharField(
        required=True, max_length=128, widget=forms.PasswordInput)
    confirmPassword = forms.CharField(
        required=True, max_length=128, widget=forms.PasswordInput)
    phoneNO = forms.CharField(required=True, max_length=10, min_length=10, validators=[RegexValidator(
        regex='^[0-9]*$', message='Phone number must be numeric 0-9 and length is 10'), ])

    def clean(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirmPassword')

        if password1 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")

        return self.cleaned_data


class signinForm(forms.Form):
    email = forms.EmailField(required=True, max_length=128)
    password = forms.CharField(
        required=True, max_length=128, widget=forms.PasswordInput)
