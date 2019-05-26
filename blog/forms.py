from django import forms
from django.contrib.auth.models import User

from .models import Blogpost



class BlogpostForm(forms.ModelForm):

    class Meta:
        model = Blogpost
        fields = ['title', 'content']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
