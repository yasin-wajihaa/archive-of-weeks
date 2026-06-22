from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    pfp = forms.ImageField(required=False,label='Profile Picture')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
