from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Room
from django.forms import ModelForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class RoomCreationForm(ModelForm):
        class Meta:
            model = Room
            fields = ['name',]