from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class UserSignupForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))

    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']


class UpdateProfileForm(forms.ModelForm):
    # first_name = forms.CharField(widget=forms.TextInput(attrs={
    #     'class':'form-control'
    # }))
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ('user',)

