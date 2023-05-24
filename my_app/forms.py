from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserModel

class SignUpForm(UserCreationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Username"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'First Name'}), max_length=32, help_text='First name')
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Last Name'}), max_length=32, help_text='Last name')
    
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':"Email"}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}))

    class Meta:
        model = UserModel
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2')



class LoginForm(forms.Form):
 
    username = forms.CharField(max_length = 30 , widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Username"}))
    password = forms.CharField(max_length=15, widget = forms.PasswordInput(attrs={'class': 'form-control','placeholder':"Password"}))