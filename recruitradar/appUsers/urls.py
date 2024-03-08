from django.urls import path
from appUsers import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('',views.home,name="Home"),
    path('login',views.login_request,name="Login"),
    path('logout',views.logout_request,name="Logout"),
    path('register',views.register,name="Register"),
    path('registro',views.registro,name="Registro"),
    path('editarusuario',views.editar_usuario,name="EditarUsuario"),
    path('aboutme',views.aboutme,name="Aboutme"),
    path('contact',views.contact,name="Contact"),

    #path('perfil',views.perfil,name="Perfil"),
    path('datos_personales',views.datos_personales,name="DatosPersonales"),
    path('noticias',views.noticias,name="Noticias"),
    path('noticias/',views.noticias,name="Noticias"),
    path('idiomas',views.idiomas,name="Idiomas"),
    path('idiomas/',views.idiomas,name="Idiomas"),
    path('eliminaridioma/<str:id>', views.eliminar_idioma, name='EliminaIdioma'),
    path('editaridioma/<str:id>', views.editar_idioma, name='EditaIdioma'),
    path('skills',views.skills,name="Skills"),
    path('skills/',views.skills,name="Skills"),
    path('eliminarskills/<str:id>', views.eliminar_skills, name='EliminaSkills'),
    path('editarskills/<str:id>', views.editar_skills, name='EditaSkills'),
    path('publicaciones',views.publicacion,name="Publicaciones"),
    path('publicaciones/',views.publicacion,name="Publicaciones"),
    path('eliminarpublicacion/<str:id>', views.eliminar_publicacion, name='EliminaPublicacion'),
    path('experiencia',views.experiencia,name="Experiencia"),
    path('experiencia/',views.experiencia,name="Experiencia"),
    path('eliminarexperienecia/<str:id>', views.eliminar_experiencia, name='EliminaExperiencia'),
    path('educacion',views.estudio,name="Educacion"),
    path('educacion/',views.estudio,name="Educacion"),
    path('eliminareducacion/<str:id>', views.eliminar_educacion, name='EliminaEducacion'),
    path('perfil',views.perfil,name="Perfil"),
    path('agregarAvatar',views.agregarAvatar,name="AgregarAvatar"),
    path('perfilde/<str:nombre>', views.perfilde, name='unperfil')
]