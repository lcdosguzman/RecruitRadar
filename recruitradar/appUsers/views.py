from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
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

def aboutme(request):
    return render(request,"appUsers/aboutme.html",{"avatar":request.session.get('foto-avatar', 'none')})

def contact(request):
    return render(request,"appUsers/contact.html",{"avatar":request.session.get('foto-avatar', 'none')})



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
def datos_personales(request):
    data_exists = DataUsuario.objects.filter(user=request.user).exists()
    if data_exists:
        data = DataUsuario.objects.get(user=request.user)
    else:
        data= DataUsuario.objects.create(user=request.user,nombre="",apellido="",bio="",
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
            exp.nombre = informacion['nombre']
            exp.apellido = informacion['apellido']
            exp.bio = informacion['bio']
            exp.telefono = informacion['telefono']
            exp.url_twitter = informacion['url_twitter']
            exp.url_facebook = informacion['url_facebook']
            exp.url_github = informacion['url_github']
            exp.url_youtube = informacion['url_youtube']
            exp.url_linkedin = informacion['url_linkedin']
            exp.save()
            miFormulario = DataUsuarioFormulario(initial={
            'nombre': informacion['nombre'],
            'apellido': informacion['apellido'],
            'bio': informacion['bio'],
            'telefono': informacion['telefono'],
            'url_twitter': informacion['url_twitter'],
            'url_facebook': informacion['url_facebook'],
            'url_github': informacion['url_github'],
            'url_youtube': informacion['url_youtube'],
            'url_linkedin': informacion['url_linkedin'],})
            data=DataUsuario.objects.get(user=request.user)
            return render(request,"AppUsers/datosPersonales.html",{"info":data,"miFormulario":miFormulario,"resp":"Datos guardados Correctamente","avatar":request.session.get('foto-avatar', 'none')})
    else:
       miFormulario = DataUsuarioFormulario(initial={
            'nombre': data.nombre,
            'apellido': data.apellido,
            'bio': data.bio,
            'telefono': data.telefono,
            'url_twitter': data.url_twitter,
            'url_facebook': data.url_facebook,
            'url_github': data.url_github,
            'url_youtube': data.url_youtube,
            'url_linkedin': data.url_linkedin,
        })

    return render(request,"AppUsers/datosPersonales.html",{"info":data,"miFormulario":miFormulario,"avatar":request.session.get('foto-avatar', 'none')})

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
def publicacion(request):
    publicacion = Publicacion.objects.filter(user=request.user)
 #manejo del post para agregar 
    if request.method == 'POST':
        miFormulario = PublicacionFormulario(request.POST,request.FILES)
        if miFormulario.is_valid():
            u = User.objects.get(username = request.user)
            informacion = miFormulario.cleaned_data
            exp = Publicacion(user=u,titulo=informacion['titulo'],contenido=informacion['contenido'],imagen=informacion['imagen'])           
            exp.save()
            miFormulario = PublicacionFormulario()
            return render(request,"appUsers/publicacion.html",{"publicacion":publicacion,"miFormulario":miFormulario,"resp":"Datos guardados Correctamente","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})
        else:
            print(miFormulario.errors)
            return render(request,"appUsers/publicacion.html",{"publicacion":publicacion,"miFormulario":miFormulario,"resp":"Datos No guardados Correctamente","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})
    else:
        miFormulario = PublicacionFormulario()

#manejo de busquedas 
    if 'pub_search' in request.GET:
        search = request.GET['pub_search']
        pubSearch = Publicacion.objects.filter(titulo__icontains=search)
        respSearch = "No se encontraron resultados para " + search
        if pubSearch.exists():
            respSearch = "Resultados para " + search
        return render(request,"appUsers/publicacion.html",{"publicacion":publicacion,"miFormulario":miFormulario,"pubSearch":pubSearch,"resp":"","respSearch":respSearch,"avatar":request.session.get('foto-avatar', 'none')})


    return render(request,"appUsers/publicacion.html",{"publicacion":publicacion,"miFormulario":miFormulario,"resp":"","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})
@login_required
def eliminar_publicacion(request,id):
    try:
        publicacion = Publicacion.objects.get(id=id)
        publicacion.delete()
    except Publicacion.DoesNotExist:
        return render(request, "appUsers/error.html", {"mensaje": "La publicación no existe."})
    
    publicaciones = Publicacion.objects.filter(user=request.user)
    miFormulario = PublicacionFormulario()

    return render(request, "appUsers/publicacion.html", {
        "publicaciones": publicaciones,
        "miFormulario": miFormulario,
        "resp": "",
        "respSearch": "",
        "avatar": request.session.get('foto-avatar', 'none')
    })

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

@login_required
def eliminar_experiencia(request,id):
    try:
        data = ExperienciaLaboral.objects.get(id=id)
        data.delete()
    except ExperienciaLaboral.DoesNotExist:
          return experiencia(request)
    
    data = ExperienciaLaboral.objects.filter(user=request.user)
    return experiencia(request)

@login_required
def eliminar_educacion(request,id):
    try:
        data = Educacion.objects.get(id=id)
        data.delete()
    except Educacion.DoesNotExist:
          return estudio(request)
    
    data = Educacion.objects.filter(user=request.user)
    return estudio(request)


@login_required
def noticias(request):
    if 'news_search' in request.GET:
        search = request.GET['news_search']
        newsSearch = Publicacion.objects.filter(titulo__icontains=search)
        respSearch = "No se encontraron resultados para " + search
        if newsSearch.exists():
            respSearch = "Resultados para " + search
        return render(request,"appUsers/noticias.html",{"newsSearch":newsSearch,"resp":"","respSearch":respSearch,"avatar":request.session.get('foto-avatar', 'none')})

    publicacion = Publicacion.objects.all().reverse()[:10]
    return render(request,"appUsers/noticias.html",{"publicacion":publicacion,"resp":"","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})

@login_required
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
                return render(request,"appUsers/experiencia.html",{"experiencias":experiencias,"miFormulario":miFormulario,"resp":"Datos guardados Correctamente","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})
            else:
                return render(request,"appUsers/experiencia.html",{"experiencias":experiencias,"miFormulario":miFormulario,"resp":"Datos No Guardados","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})
    else:
        miFormulario = ExperienciaFormulario()
    
    if 'text_search' in request.GET:
        search = request.GET['text_search']
        experienciaSearch = ExperienciaLaboral.objects.filter(description__icontains=search)
        respSearch = "No se encontraron resultados para " + search
        if experienciaSearch.exists():
            respSearch = "Resultados para " + search
        return render(request,"appUsers/experiencia.html",{"experiencias":experiencias,"miFormulario":miFormulario,"experienciaSearch":experienciaSearch,"resp":"","respSearch":respSearch,"avatar":request.session.get('foto-avatar', 'none')})

    return render(request,"appUsers/experiencia.html",{"experiencias":experiencias,"miFormulario":miFormulario,"resp":"","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})

@login_required
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
                return render(request,"appUsers/educacion.html",{"estudios":estudios,"miFormulario":miFormulario,"resp":"Datos guardados Correctamente","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})
        else:
          return render(request,"appUsers/educacion.html",{"estudios":estudios,"miFormulario":miFormulario,"resp":"Datos no guardados Correctamente","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})
    else:
        miFormulario = EstudioFormulario()

    if 'text_search' in request.GET:
        search = request.GET['text_search']
        estudiosSearch = Educacion.objects.filter(description__icontains=search)
        respSearch = "No se encontraron resultados para " + search
        if estudiosSearch.exists():
            respSearch = "Resultados para " + search
        return render(request,"appUsers/educacion.html",{"estudios":estudios,"miFormulario":miFormulario,"estudiosSearch":estudiosSearch,"resp":"","respSearch":respSearch,"avatar":request.session.get('foto-avatar', 'none')})

    return render(request,"appUsers/educacion.html",{"estudios":estudios,"miFormulario":miFormulario,"resp":"","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})

@login_required
def perfil(request):
    
    experiencias = ExperienciaLaboral.objects.filter(user=request.user)
    estudios = Educacion.objects.filter(user=request.user)
    skills = Skills.objects.filter(user=request.user)
    idiomas = Idiomas.objects.filter(user=request.user)
    try:
        perfil=DataUsuario.objects.get(user=request.user)
    except DataUsuario.DoesNotExist:
        perfil=""
    
    return render(request,"appUsers/perfil.html",{"experiencias":experiencias,"estudios":estudios,"idiomas":idiomas,"perfil":perfil,"skills":skills,"avatar":request.session.get('foto-avatar', 'none')})

@login_required
def agregarAvatar(request):
 
    if request.method == 'POST':
        miFormulario = AvatarFormulario(request.POST,request.FILES)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            try:
                exp = Avatar.objects.get(user=request.user)
            except Avatar.DoesNotExist:
                exp = Avatar(user=request.user, imagen=informacion['imagen'])
                exp.save()
            else:
                exp.imagen = informacion['imagen']

                exp.save()
            set_session_foto(request)
            miFormulario = AvatarFormulario
            return render(request,"appUsers/avatar.html",{"miFormulario":miFormulario,"resp":"Datos guardados Correctamente","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})
        else:
            return render(request,"appUsers/avatar.html",{"miFormulario":miFormulario,"resp":"Datos No guardados Correctamente","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})
    else:
        miFormulario = AvatarFormulario()
        return render(request,"appUsers/avatar.html",{"miFormulario":miFormulario,"avatar":request.session.get('foto-avatar', 'none')})

def perfilde(request, nombre):

    usuarios = User.objects.filter(username=nombre)
    if usuarios.exists():
        usuario_encontrado = usuarios.first()
        user_id = usuario_encontrado.id
        experiencias = ExperienciaLaboral.objects.filter(user=user_id)
        estudios = Educacion.objects.filter(user=user_id)
        skills = Skills.objects.filter(user=user_id)
        idiomas = Idiomas.objects.filter(user=user_id)
        try:
            avatar=Avatar.objects.get(user=user_id)
        except Avatar.DoesNotExist:
            avatar="/media/avatares/default.jpg"
        try:
            perfil=DataUsuario.objects.get(user=user_id)
        except DataUsuario.DoesNotExist:
            perfil=""
        print(avatar)    
        return render(request,"appUsers/perfilde.html",{"foto_avatar":avatar.imagen.url,"experiencias":experiencias,"estudios":estudios,"idiomas":idiomas,"perfil":perfil,"skills":skills,"avatar":request.session.get('foto-avatar', 'none'),"enc":"1"})
       
    else:
        return render(request, "appUsers/perfilde.html", {"foto_avatar":"","nombredeparametro": nombre,"enc":"0","avatar":request.session.get('foto-avatar', 'none')})