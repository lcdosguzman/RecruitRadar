from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.models import User
from .models import Avatar,Publicacion
  
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir Contraseña",widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar email")
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir Contraseña",widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email','password1','password2']        
