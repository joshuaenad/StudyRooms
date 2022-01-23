from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Room, User


class MyUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class RoomForm(ModelForm):

    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio', ]


# class UserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True, label='E-mail')

#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2")
