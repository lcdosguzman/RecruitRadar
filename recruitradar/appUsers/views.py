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

# Create your views here.
def home(request):
    publicacion = Publicacion.objects.all().reverse()[:10]
    return render(request,"appUsers/home.html" ,{"publicacion":publicacion,"avatar":request.session.get('foto-avatar', 'none')})

def login_request(request):
    print("intento de login")
    if request.method == 'POST':
            miFormulario = AuthenticationForm(request, data=request.POST)
            if miFormulario.is_valid():
                usuario = miFormulario.cleaned_data.get('username')
                passw = miFormulario.cleaned_data.get('password')

                user = authenticate(username=usuario, password=passw)

                if user is not None:
                    print("login correcto ahora debo ir a curriculos")
                    login(request,user)
                    publicacion = Publicacion.objects.all().reverse()[:10]
                    set_session_foto(request)
                    return render(request,"appUsers/noticias.html",{"publicacion":publicacion,"resp":"","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})
                else:
                    print("no encontrado")
                    return render(request,"appUsers/login",{"miFormulario":miFormulario,"avatar":request.session.get('foto-avatar', 'none')}) 
            else:
                print("formulario no valido")
                return render(request,"appUsers/login.html",{"miFormulario":miFormulario,"avatar":request.session.get('foto-avatar', 'none')})
     
    print("primera vez")
    miFormulario = AuthenticationForm()
    return render(request,"appUsers/login.html",{"miFormulario":miFormulario,"avatar":request.session.get('foto-avatar', 'none')}) 

def set_session_foto(request):
   
    try:
        avatar = Avatar.objects.get(user=request.user)
        print(avatar.imagen.url)
        request.session['foto-avatar'] = avatar.imagen.url
    except Avatar.DoesNotExist:
        request.session['foto-avatar'] ="/media/avatares/default.jpg"
    
    return

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
    
def editar_skills(request,id):
    resp=""
    skillsdata = Skills.objects.get(id=id)
    if request.method == 'POST':
        form = SkillFormulario(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            skillsdata.aptitud = data['aptitud']
            skillsdata.save()
            skills = Skills.objects.filter(user=request.user)
            miFormulario = SkillFormulario()
            return render(request,"appUsers/skills.html",{"miFormulario":miFormulario,"skills":skills,"resp":resp,"form":form,"avatar":request.session.get('foto-avatar', 'none')})
        else:
            resp="datos no validos"
            form = SkillFormulario(initial={'aptitud':skillsdata.aptitud})
            return render(request,"appUsers/editarskills.html",{"resp":resp,"form":form,"avatar":request.session.get('foto-avatar', 'none')})
    
    form = SkillFormulario(initial={'aptitud':skillsdata.aptitud})      
    return render(request,"appUsers/editarskills.html",{"resp":resp,"form":form,"avatar":request.session.get('foto-avatar', 'none')})

def editar_idioma(request,id):
    resp=""
    idiomadata = Idiomas.objects.get(id=id)
    if request.method == 'POST':
        form = IdiomaFormulario(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            idiomadata.idioma = data['idioma']
            idiomadata.nivel = data['nivel']
            idiomadata.save()
            idiomas = Idiomas.objects.filter(user=request.user)
            miFormulario = IdiomaFormulario()
            return render(request,"appUsers/idiomas.html",{"miFormulario":miFormulario,"idiomas":idiomas,"resp":resp,"form":form,"avatar":request.session.get('foto-avatar', 'none')})
        else:
            resp="datos no validos"
            form = IdiomaFormulario(initial={'idioma':idiomadata.idioma,'nivel':idiomadata.nivel})
            return render(request,"appUsers/editaridioma.html",{"resp":resp,"form":form,"avatar":request.session.get('foto-avatar', 'none')})
    
    form = IdiomaFormulario(initial={'idioma':idiomadata.idioma,'nivel':idiomadata.nivel})      
    return render(request,"appUsers/editaridioma.html",{"resp":resp,"form":form,"avatar":request.session.get('foto-avatar', 'none')})

def registro(request):
    return render(request,"appUsers/registro.html")

# Vistas Limitadas a usuarios Logueados
@login_required
def logout_request(request):
    logout(request)
    return home(request)

@login_required
def idiomas(request):
    idiomas = Idiomas.objects.filter(user=request.user)
    if request.method == 'POST':
        miFormulario = IdiomaFormulario(request.POST)
        if miFormulario.is_valid():
            u = User.objects.get(username = request.user)
            informacion = miFormulario.cleaned_data
            exp = Idiomas(user=u,idioma=informacion['idioma'],nivel=informacion['nivel'])
            exp.save()
            miFormulario = IdiomaFormulario()
            return render(request,"appUsers/idiomas.html",{"idiomas":idiomas,"miFormulario":miFormulario,"resp":"Datos guardados Correctamente","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})
    else:
        miFormulario = IdiomaFormulario()

    if 'text_search' in request.GET:
        search = request.GET['text_search']
        idiomaSearch = Idiomas.objects.filter(idioma__icontains=search)
        respSearch = "No se encontraron resultados para " + search
        if idiomaSearch.exists():
            respSearch = "Resultados para " + search
        return render(request,"appUsers/idiomas.html",{"idiomas":idiomas,"miFormulario":miFormulario,"idiomaSearch":idiomaSearch,"resp":"","respSearch":respSearch,"avatar":request.session.get('foto-avatar', 'none')})

    return render(request,"appUsers/idiomas.html",{"idiomas":idiomas,"miFormulario":miFormulario,"resp":"","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})

@login_required
def skills(request):
    skills = Skills.objects.filter(user=request.user)
 #manejo del post para agregar 
    if request.method == 'POST':
        miFormulario = SkillFormulario(request.POST)
        if miFormulario.is_valid():
            u = User.objects.get(username = request.user)
            informacion = miFormulario.cleaned_data
            exp = Skills(user=u,aptitud=informacion['aptitud'])
            exp.save()
            miFormulario = SkillFormulario()
            return render(request,"appUsers/skills.html",{"skills":skills,"miFormulario":miFormulario,"resp":"Datos guardados Correctamente","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})
        else:
            return render(request,"appUsers/skills.html",{"skills":skills,"miFormulario":miFormulario,"resp":"Datos No guardados Correctamente","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})
    else:
        miFormulario = SkillFormulario()

#manejo de busquedas 
    if 'skill_search' in request.GET:
        search = request.GET['skill_search']
        skillsSearch = Skills.objects.filter(aptitud__icontains=search)
        respSearch = "No se encontraron resultados para " + search
        if skillsSearch.exists():
            respSearch = "Resultados para " + search
        return render(request,"appUsers/skills.html",{"skills":skills,"miFormulario":miFormulario,"skillsSearch":skillsSearch,"resp":"","respSearch":respSearch,"avatar":request.session.get('foto-avatar', 'none')})


    return render(request,"appUsers/skills.html",{"skills":skills,"miFormulario":miFormulario,"resp":"","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})

@login_required
def eliminar_skills(request,id):
    try:
        skillsdata = Skills.objects.get(id=id)
        skillsdata.delete()
    except Skills.DoesNotExist:
        return skills(request)
    
    skillsdata = Skills.objects.filter(user=request.user)
    return skills(request)
   
@login_required
def eliminar_idioma(request,id):
    try:
        idiomadata = Idiomas.objects.get(id=id)
        idiomadata.delete()
    except idiomas.DoesNotExist:
          return idiomas(request)
    
    idiomadata = Idiomas.objects.filter(user=request.user)
    return idiomas(request)




    

 #Listas Basadas en Clases
    