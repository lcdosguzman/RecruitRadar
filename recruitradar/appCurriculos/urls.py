from django.urls import path
from appCurriculos import views
from django.contrib.auth.views import *

urlpatterns = [
    #url publica
    path('',views.home,name="Home"),
    path('aboutme',views.aboutme,name="Aboutme"),
    path('contact',views.contact,name="Contact"),
    #Datos Personales
    path('datos_personales',views.datos_personales,name="DatosPersonales"),
    path('agregarAvatar',views.agregarAvatar,name="AgregarAvatar"),
    path('perfil',views.perfil,name="Perfil"), #Perfil Muestra el Curriculo del usuario
    path('perfilde/<str:nombre>', views.perfilde, name='unperfil'),
    #Skill
    path('skill/', views.SkillListView.as_view(), name='skill_list'),
    path('skill/crear/', views.SkillCreateView.as_view(), name='skill_create'),
    path('skill/<int:pk>/', views.SkillDetailView.as_view(), name='skill_detalle'),
    path('skill/editar/<int:pk>/', views.SkillUpdateView.as_view(), name='skill_update'),
    path('skill/eliminar/<int:pk>/', views.SkillDeleteView.as_view(), name='skill_delete'),
    #Idiomas
    path('idioma/', views.IdiomaListView.as_view(), name='idioma_list'),
    path('idioma/crear/', views.IdiomaCreateView.as_view(), name='idioma_create'),
    path('idioma/<int:pk>/', views.IdiomaDetailView.as_view(), name='idioma_detalle'),
    path('idioma/editar/<int:pk>/', views.IdiomaUpdateView.as_view(), name='idioma_update'),
    path('idioma/eliminar/<int:pk>/', views.IdiomaDeleteView.as_view(), name='idioma_delete'),
    #Educacion
    path('educacion',views.estudio,name="Educacion"),
    path('educacion/',views.estudio,name="EducacionSearch"),
    path('eliminareducacion/<str:id>', views.eliminar_educacion, name='EliminaEducacion'),
    path('editareducacion/<str:id>', views.editar_educacion, name='EditaEducacion'),
    #Experiencia
    path('experiencia',views.experiencia,name="Experiencia"),
    path('experiencia/',views.experiencia,name="ExperienciaSearch"),
    path('eliminarexperiencia/<str:id>', views.eliminar_experiencia, name='EliminaExperiencia'),
    path('editarexperiencia/<str:id>', views.editar_experiencia, name='EditaExperiencia'),
    #Publicaciones
    path('publicaciones',views.publicacion,name="Publicaciones"),
    path('publicaciones/',views.publicacion,name="PublicacionSearch"),
    path('eliminarpublicacion/<str:id>', views.eliminar_publicacion, name='EliminaPublicacion'),
    path('editarpublicacion/<str:id>', views.editar_publicacion, name='EditaPublicacion'),
    #Noticias: Es una lista de las publicaciones de los usuarios
    path('noticias',views.noticias,name="Noticias"),
    path('noticias/',views.noticias,name="NoticiasSearch"),

    


    
]