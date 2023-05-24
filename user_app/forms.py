from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from my_app.forms import SignUpForm
class InputForm(forms.Form):
 
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    roll_number = forms.IntegerField(
                     help_text = "Enter 6 digit roll number"
                     )
    password = forms.CharField(widget = forms.PasswordInput())


class UpdateUser(SignUpForm):
    sponsor = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Sponsor Username", "readonly": True}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Username","readonly": True}))
