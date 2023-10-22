from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2","first_name", "last_name")
    
    username = forms.CharField(label="Username")
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password",)
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"