from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from appUsers.models import *
from appUsers.forms import *
from appCurriculos.views import set_session_foto,home

# Create your views here.


def login_request(request):
    if request.method == 'POST':
            miFormulario = AuthenticationForm(request, data=request.POST)
            if miFormulario.is_valid():
                usuario = miFormulario.cleaned_data.get('username')
                passw = miFormulario.cleaned_data.get('password')
                user = authenticate(username=usuario, password=passw)

                if user is not None:
                    login(request,user)
                    publicacion = Publicacion.objects.all().reverse()[:10]
                    set_session_foto(request)
                    return render(request,"appCurriculos/noticias.html",{"publicacion":publicacion,"resp":"","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})
                else:
                    return render(request,"appUsers/login",{"miFormulario":miFormulario,"avatar":request.session.get('foto-avatar', 'none')}) 
            else:
                return render(request,"appUsers/login.html",{"miFormulario":miFormulario,"avatar":request.session.get('foto-avatar', 'none')})
     
    miFormulario = AuthenticationForm()
    return render(request,"appUsers/login.html",{"miFormulario":miFormulario,"avatar":request.session.get('foto-avatar', 'none')}) 

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render (request,"appUsers/home.html",{"mensaje":"Usuario Creado"})
    else:
        form = UserRegisterForm()

    return render(request,"appUsers/registro.html",{"form":form})

@login_required
def editar_usuario(request):
    resp=""
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST,instance=usuario)
        if form.is_valid():
            data = form.cleaned_data
            usuario.email = data['email']
            usuario = form.save(commit=False)
            nueva_contraseña = form.cleaned_data.get('password')
            if nueva_contraseña:
                usuario.set_password(nueva_contraseña)

            usuario.save()
            resp="los datos fueron cambiados"
        else:
            resp="datos no validos"
            form = UserEditForm(initial={'email':usuario.email})
            return render(request,"appUsers/editarusuario.html",{"resp":resp,"form":form,"avatar":request.session.get('foto-avatar', 'none')})
    
    form = UserEditForm(initial={'email':usuario.email})      
    return render(request,"appUsers/editarusuario.html",{"resp":resp,"form":form,"avatar":request.session.get('foto-avatar', 'none')})

@login_required
def logout_request(request):
    logout(request)
    return home(request)
