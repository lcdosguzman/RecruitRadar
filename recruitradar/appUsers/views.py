from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from appUsers.models import *
from appUsers.forms import *

# Create your views here.
def home(request):
    publicacion = Publicacion.objects.all().reverse()[:10]
    return render(request,"appUsers/home.html" ,{"publicacion":publicacion})

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
                    return render(request,"appCurriculos/admin_home.html") 
                else:
                    print("no encontrado")
                    return render(request,"appUsers/login",{"miFormulario":miFormulario}) 
            else:
                print("formulario no valido")
                return render(request,"appUsers/login.html",{"miFormulario":miFormulario})
     
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
            return render(request,"appUsers/idiomas.html",{"idiomas":idiomas,"miFormulario":miFormulario,"resp":"Datos guardados Correctamente","respSearch":""})
    else:
        miFormulario = IdiomaFormulario()

    if 'text_search' in request.GET:
        search = request.GET['text_search']
        idiomaSearch = Idiomas.objects.filter(idioma__icontains=search)
        respSearch = "No se encontraron resultados para " + search
        if idiomaSearch.exists():
            respSearch = "Resultados para " + search
        return render(request,"appUsers/idiomas.html",{"idiomas":idiomas,"miFormulario":miFormulario,"idiomaSearch":idiomaSearch,"resp":"","respSearch":respSearch})

    return render(request,"appUsers/idiomas.html",{"idiomas":idiomas,"miFormulario":miFormulario,"resp":"","respSearch":""})
@login_required
def datos_personales(request):
    data_exists = DataUsuario.objects.filter(user=request.user).exists()
    if data_exists:
        data = DataUsuario.objects.get(user=request.user)
    else:
        data= DataUsuario.objects.create(user=request.user,bio="",
                                         telefono="",
                                         url_twitter="",
                                         url_facebook="",
                                         url_github="",
                                         url_youtube="",
                                         url_linkedin="")
    
    if request.method == 'POST':
        miFormulario = DataUsuarioFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            exp = DataUsuario.objects.get(user=request.user)
            exp.bio = informacion['bio']
            exp.telefono = informacion['telefono']
            exp.url_twitter = informacion['url_twitter']
            exp.url_facebook = informacion['url_facebook']
            exp.url_github = informacion['url_github']
            exp.url_youtube = informacion['url_youtube']
            exp.url_linkedin = informacion['url_linkedin']
            exp.save()
            miFormulario = DataUsuarioFormulario(initial={
            'bio': informacion['bio'],
            'telefono': informacion['telefono'],
            'url_twitter': informacion['url_twitter'],
            'url_facebook': informacion['url_facebook'],
            'url_github': informacion['url_github'],
            'url_youtube': informacion['url_youtube'],
            'url_linkedin': informacion['url_linkedin'],})
            data=DataUsuario.objects.get(user=request.user)
            return render(request,"AppUsers/datosPersonales.html",{"info":data,"miFormulario":miFormulario,"resp":"Datos guardados Correctamente"})
    else:
       miFormulario = DataUsuarioFormulario(initial={
            'bio': data.bio,
            'telefono': data.telefono,
            'url_twitter': data.url_twitter,
            'url_facebook': data.url_facebook,
            'url_github': data.url_github,
            'url_youtube': data.url_youtube,
            'url_linkedin': data.url_linkedin,
        })

    return render(request,"AppUsers/datosPersonales.html",{"info":data,"miFormulario":miFormulario})


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
            return render(request,"appUsers/skills.html",{"skills":skills,"miFormulario":miFormulario,"resp":"Datos guardados Correctamente","respSearch":""})
        else:
            return render(request,"appUsers/skills.html",{"skills":skills,"miFormulario":miFormulario,"resp":"Datos No guardados Correctamente","respSearch":""})
    else:
        miFormulario = SkillFormulario()

#manejo de busquedas 
    if 'skill_search' in request.GET:
        search = request.GET['skill_search']
        skillsSearch = Skills.objects.filter(aptitud__icontains=search)
        respSearch = "No se encontraron resultados para " + search
        if skillsSearch.exists():
            respSearch = "Resultados para " + search
        return render(request,"appUsers/skills.html",{"skills":skills,"miFormulario":miFormulario,"skillsSearch":skillsSearch,"resp":"","respSearch":respSearch})


    return render(request,"appUsers/skills.html",{"skills":skills,"miFormulario":miFormulario,"resp":"","respSearch":""})

@login_required
def publicacion(request):
    publicacion = Publicacion.objects.filter(user=request.user)
 #manejo del post para agregar 
    if request.method == 'POST':
        miFormulario = PublicacionFormulario(request.POST)
        if miFormulario.is_valid():
            u = User.objects.get(username = request.user)
            informacion = miFormulario.cleaned_data
            exp = Publicacion(user=u,titulo=informacion['titulo'],contenido=informacion['contenido'])
            exp.save()
            miFormulario = PublicacionFormulario()
            return render(request,"appUsers/publicacion.html",{"publicacion":publicacion,"miFormulario":miFormulario,"resp":"Datos guardados Correctamente","respSearch":""})
        else:
            return render(request,"appUsers/publicacion.html",{"publicacion":publicacion,"miFormulario":miFormulario,"resp":"Datos No guardados Correctamente","respSearch":""})
    else:
        miFormulario = PublicacionFormulario()

#manejo de busquedas 
    if 'pub_search' in request.GET:
        search = request.GET['pub_search']
        pubSearch = Publicacion.objects.filter(titulo__icontains=search)
        respSearch = "No se encontraron resultados para " + search
        if pubSearch.exists():
            respSearch = "Resultados para " + search
        return render(request,"appUsers/publicacion.html",{"publicacion":publicacion,"miFormulario":miFormulario,"pubSearch":pubSearch,"resp":"","respSearch":respSearch})


    return render(request,"appUsers/publicacion.html",{"publicacion":publicacion,"miFormulario":miFormulario,"resp":"","respSearch":""})

@login_required
def home_self(request):
    if 'news_search' in request.GET:
        search = request.GET['news_search']
        newsSearch = Publicacion.objects.filter(titulo__icontains=search)
        respSearch = "No se encontraron resultados para " + search
        if newsSearch.exists():
            respSearch = "Resultados para " + search
        return render(request,"appUsers/noticias.html",{"newsSearch":newsSearch,"resp":"","respSearch":respSearch})

    publicacion = Publicacion.objects.all().reverse()[:10]
    return render(request,"appUsers/noticias.html",{"publicacion":publicacion,"resp":"","respSearch":""})

def experiencia(request):
    experiencias = ExperienciaLaboral.objects.filter(user=request.user)
    if request.method == 'POST':
        miFormulario = ExperienciaFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            if 'periodo_inicio'in request.POST:
                u = User.objects.get(username = request.user)
                informacion = miFormulario.cleaned_data
                exp = ExperienciaLaboral (user=u,cargo=informacion['cargo'],empresa=informacion['empresa'],periodo_fin=informacion['periodo_fin'],periodo_inicio=informacion['periodo_inicio'],description=informacion['description'],pais=informacion['pais'])
                exp.save()
                miFormulario = ExperienciaFormulario()
                return render(request,"appUsers/experiencia.html",{"experiencias":experiencias,"miFormulario":miFormulario,"resp":"Datos guardados Correctamente","respSearch":""})
            else:
                return render(request,"appUsers/experiencia.html",{"experiencias":experiencias,"miFormulario":miFormulario,"resp":"Datos No Guardados","respSearch":""})
    else:
        miFormulario = ExperienciaFormulario()
    
    if 'text_search' in request.GET:
        search = request.GET['text_search']
        experienciaSearch = ExperienciaLaboral.objects.filter(description__icontains=search)
        respSearch = "No se encontraron resultados para " + search
        if experienciaSearch.exists():
            respSearch = "Resultados para " + search
        return render(request,"appUsers/experiencia.html",{"experiencias":experiencias,"miFormulario":miFormulario,"experienciaSearch":experienciaSearch,"resp":"","respSearch":respSearch})

    return render(request,"appUsers/experiencia.html",{"experiencias":experiencias,"miFormulario":miFormulario,"resp":"","respSearch":""})

def estudio(request):
    estudios = Educacion.objects.filter(user=request.user)
    if request.method == 'POST':
        miFormulario = EstudioFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
                u = User.objects.get(username = request.user)
                informacion = miFormulario.cleaned_data
                exp = Educacion(user=u,institucion=informacion['institucion'],titulo=informacion['titulo'],periodo_fin=int(informacion['periodo_fin']),periodo_inicio=int(informacion['periodo_inicio']),description=informacion['description'],pais=informacion['pais'])
                exp.save()
                miFormulario = EstudioFormulario()
                return render(request,"appUsers/educacion.html",{"estudios":estudios,"miFormulario":miFormulario,"resp":"Datos guardados Correctamente","respSearch":""})
        else:
          return render(request,"appUsers/educacion.html",{"estudios":estudios,"miFormulario":miFormulario,"resp":"Datos no guardados Correctamente","respSearch":""})
    else:
        miFormulario = EstudioFormulario()

    if 'text_search' in request.GET:
        search = request.GET['text_search']
        estudiosSearch = Educacion.objects.filter(description__icontains=search)
        respSearch = "No se encontraron resultados para " + search
        if estudiosSearch.exists():
            respSearch = "Resultados para " + search
        return render(request,"appUsers/educacion.html",{"estudios":estudios,"miFormulario":miFormulario,"estudiosSearch":estudiosSearch,"resp":"","respSearch":respSearch})

    return render(request,"appUsers/educacion.html",{"estudios":estudios,"miFormulario":miFormulario,"resp":"","respSearch":""})