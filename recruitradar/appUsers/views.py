from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from appUsers.models import *
from appUsers.forms import *

# Create your views here.
def home(request):
    return render(request,"appUsers/home.html")
#
#def login(request):
#    return render(request,"appUsers/login.html")

def login_request(request):
    print("intento de login")
    if request.method == 'POST':
            miFormulario = AuthenticationForm(request, data=request.POST)
            if miFormulario.is_valid():
                usuario = miFormulario.cleaned_data.get('username')
                passw = miFormulario.cleaned_data.get('password')

                user = authenticate(username=usuario, password=passw)

                if user is not None:
                    print("login correcto")
                    login(request,user)
                    return render(request,"appUsers/home.html") 
                else:
                    print("no encontrado")
                    return render(request,"appUsers/usercorrecto",{"miFormulario":miFormulario}) 
            else:
                print("formulario no valido")
                return render(request,"appUsers/contact.html")
     
    print("primera vez")
    miFormulario = AuthenticationForm()
    return render(request,"appUsers/login.html",{"miFormulario":miFormulario}) 

def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render (request,"appUsers/home.html",{"mensaje":"Usuario Creado"})
    else:
        #form = UserCreationForm()
        form = UserRegisterForm()

    return render(request,"appUsers/registro.html",{"form":form})

def registro(request):
    return render(request,"appUsers/registro.html")

def aboutme(request):
    return render(request,"appUsers/aboutme.html")

def contact(request):
    return render(request,"appUsers/contact.html")
@login_required
def logout_request(request):
    logout(request)
    return render(request,"appUsers/logout.html")
