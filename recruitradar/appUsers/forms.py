from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class CAuthenticationForm(AuthenticationForm):
    # Puedes agregar campos adicionales o personalizar el formulario según tus necesidades
    # Por ejemplo, puedes agregar un campo de "Recordar sesión" (remember me)
    cargo = forms.CharField(label='Cargo', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej: Programador Backend Ssr'}))
    empresa = forms.CharField(label='Empresa', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'La Compañia S.A.'}))
    remember_me = forms.BooleanField(required=False, initial=True, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir Contraseña",widget=forms.PasswordInput)

   