from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from.models import Profile
from django.utils.translation import gettext_lazy as _

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='E-Mail Address')
    username = forms.CharField(label='Username', min_length=3, max_length=50)  
    first_name = forms.CharField(label='First Name', min_length=1, max_length=50)
    last_name = forms.CharField(label='Last Name', min_length=1, max_length=50)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)  

    class Meta:
            model = User
            fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
          email = forms.EmailField()
          class Meta:
              model = User
              fields = ['email', 'first_name', 'last_name']

class ProfileUpdateForm (forms.ModelForm):
            class Meta:
                model = Profile
                fields = ['image']