from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.models import User
from .models import Avatar,Publicacion
  
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Usuario", max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Contraseña", max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2= forms.CharField(label="Repetir Contraseña", max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar email", max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Contraseña",max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2= forms.CharField(label="Repetir Contraseña",max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email','password1','password2']        
