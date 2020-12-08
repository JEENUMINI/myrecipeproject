from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]

class loginForm(forms.Form):
    username=forms.CharField(max_length=150)
    password=forms.CharField(max_length=120)

class ProfileCreateForm(ModelForm):
    user=forms.CharField(widget=forms.TextInput(attrs={"readonly":"readonly"}))
    class Meta:
        model=Profile
        fields=["user","profile_pic","bio","birth_date"]
