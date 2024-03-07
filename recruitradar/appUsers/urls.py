from django.urls import path
from appUsers import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.home,name="Home"),
    path('login',views.login_request,name="Login"),
    path('logout',views.logout_request,name="Logout"),
    path('register',views.register,name="Register"),
    path('registro',views.registro,name="Registro"),
    path('aboutme',views.aboutme,name="Aboutme"),
    path('contact',views.contact,name="Contact"),

    #path('perfil',views.perfil,name="Perfil"),
    path('datos_personales',views.datos_personales,name="DatosPersonales"),
    path('noticias',views.noticias,name="Noticias"),
    path('noticias/',views.noticias,name="Noticias"),
    path('idiomas',views.idiomas,name="Idiomas"),
    path('idiomas/',views.idiomas,name="Idiomas"),
    path('skills',views.skills,name="Skills"),
    path('skills/',views.skills,name="Skills"),
    path('publicaciones',views.publicacion,name="Publicaciones"),
    path('publicaciones/',views.publicacion,name="Publicaciones"),
    path('experiencia',views.experiencia,name="Experiencia"),
    path('experiencia/',views.experiencia,name="Experiencia"),
    path('educacion',views.estudio,name="Educacion"),
    path('educacion/',views.estudio,name="Educacion"),
    path('perfil',views.perfil,name="Perfil"),
    path('agregarAvatar',views.agregarAvatar,name="AgregarAvatar"),
]