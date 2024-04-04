from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from appUsers.models import *
from appUsers.forms import *
from appCurriculos.models import *
from appCurriculos.forms import *

# Create your views here.
def aboutme(request):
    return render(request,"appCurriculos/aboutme.html",{"avatar":request.session.get('foto-avatar', 'none')})

def contact(request):
    return render(request,"appCurriculos/contact.html",{"avatar":request.session.get('foto-avatar', 'none')})

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
        return render(request,"appCurriculos/perfilde.html",{"foto_avatar":avatar.imagen.url,"experiencias":experiencias,"estudios":estudios,"idiomas":idiomas,"perfil":perfil,"skills":skills,"avatar":request.session.get('foto-avatar', 'none'),"enc":"1"})
       
    else:
        return render(request, "appCurriculos/perfilde.html", {"foto_avatar":"","nombredeparametro": nombre,"enc":"0","avatar":request.session.get('foto-avatar', 'none')})
    
def home(request):
    publicacion = Publicacion.objects.all().reverse()[:10]
    return render(request,"appCurriculos/home.html" ,{"publicacion":publicacion,"avatar":request.session.get('foto-avatar', 'none')})

@login_required
def eliminar_publicacion(request,id):
    try:
        publicacions = Publicacion.objects.get(id=id)
        publicacions.delete()
    except Publicacion.DoesNotExist:
        return redirect('Publicaciones')
    
    publicacions = Publicacion.objects.filter(user=request.user)
    return redirect('Publicaciones')

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
            return render(request,"appCurriculos/publicacion.html",{"publicacion":publicacion,"miFormulario":miFormulario,"resp":"Datos guardados Correctamente","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})
        else:
            print(miFormulario.errors)
            return render(request,"appCurriculos/publicacion.html",{"publicacion":publicacion,"miFormulario":miFormulario,"resp":"Datos No guardados Correctamente","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})
    else:
        miFormulario = PublicacionFormulario()

#manejo de busquedas 
    if 'pub_search' in request.GET:
        search = request.GET['pub_search']
        pubSearch = Publicacion.objects.filter(titulo__icontains=search,user=request.user)
        respSearch = "No se encontraron resultados para " + search
        if pubSearch.exists():
            respSearch = "Resultados para " + search
        return render(request,"appCurriculos/publicacion.html",{"publicacion":publicacion,"miFormulario":miFormulario,"pubSearch":pubSearch,"resp":"","respSearch":respSearch,"avatar":request.session.get('foto-avatar', 'none')})


    return render(request,"appCurriculos/publicacion.html",{"publicacion":publicacion,"miFormulario":miFormulario,"resp":"","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})

@login_required
def editar_publicacion(request,id):
    resp=""
    data = Publicacion.objects.get(id=id)
    if request.method == 'POST':
        form = PublicacionFormulario(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            dataf = form.cleaned_data
            data.titulo = dataf['titulo']
            data.contenido = dataf['contenido']
            data.imagen = dataf['imagen']
            data.save()
            publicaciones = Publicacion.objects.filter(user=request.user)
            miFormulario = PublicacionFormulario()
            return redirect('Publicaciones')
        else:
            resp="datos no validos"
            form = PublicacionFormulario(initial={'titulo':data.titulo,'contenido':data.contenido,'imagen':data.imagen})
            return render(request,"appCurriculos/editarpublicacion.html",{"resp":resp,"form":form,"avatar":request.session.get('foto-avatar', 'none')})
    
    form = PublicacionFormulario(initial={'titulo':data.titulo,'contenido':data.contenido,'imagen':data.imagen})      
    return render(request,"appCurriculos/editarpublicacion.html",{"resp":resp,"form":form,"avatar":request.session.get('foto-avatar', 'none')})

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
            return render(request,"appCurriculos/datosPersonales.html",{"info":data,"miFormulario":miFormulario,"resp":"Datos guardados Correctamente","avatar":request.session.get('foto-avatar', 'none')})
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

    return render(request,"appCurriculos/datosPersonales.html",{"info":data,"miFormulario":miFormulario,"avatar":request.session.get('foto-avatar', 'none')})

@login_required
def noticias(request):
    if 'news_search' in request.GET:
        search = request.GET['news_search']
        newsSearch = Publicacion.objects.filter(titulo__icontains=search)
        respSearch = "No se encontraron resultados para " + search
        if newsSearch.exists():
            respSearch = "Resultados para " + search
        return render(request,"appCurriculos/noticias.html",{"newsSearch":newsSearch,"resp":"","respSearch":respSearch,"avatar":request.session.get('foto-avatar', 'none')})

    publicacion = Publicacion.objects.all().reverse()[:10]
    return render(request,"appCurriculos/noticias.html",{"publicacion":publicacion,"resp":"","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})

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
    
    return render(request,"appCurriculos/perfil.html",{"experiencias":experiencias,"estudios":estudios,"idiomas":idiomas,"perfil":perfil,"skills":skills,"avatar":request.session.get('foto-avatar', 'none')})

@login_required
def agregarAvatar(request):
 
    if request.method == 'POST':
        miFormulario = AvatarFormulario(request.POST,request.FILES)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            imagen = informacion.get('imagen') 
            if not imagen:  
                return render(request, "appCurriculos/avatar.html", {"miFormulario": miFormulario, "resp": "Por favor, seleccione una imagen", "respSearch": "", "avatar": request.session.get('foto-avatar', 'none')})

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
            return render(request,"appCurriculos/avatar.html",{"miFormulario":miFormulario,"resp":"Datos guardados Correctamente","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})
        else:
            return render(request,"appCurriculos/avatar.html",{"miFormulario":miFormulario,"resp":"Datos No guardados Correctamente","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})
    else:
        miFormulario = AvatarFormulario()
        return render(request,"appCurriculos/avatar.html",{"miFormulario":miFormulario,"avatar":request.session.get('foto-avatar', 'none')})

@login_required
def set_session_foto(request):
   
    try:
        avatar = Avatar.objects.get(user=request.user)
        print(avatar.imagen.url)
        request.session['foto-avatar'] = avatar.imagen.url
    except Avatar.DoesNotExist:
        request.session['foto-avatar'] ="/media/avatares/default.jpg"
    
    return
    
