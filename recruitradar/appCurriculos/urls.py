from django.urls import path
from appCurriculos.views.views_other import *
from appCurriculos.views.views_skills import *
from django.contrib.auth.views import *

urlpatterns = [
    #url publica
    path('',home,name="Home"),
    path('aboutme',aboutme,name="Aboutme"),
    path('contact',contact,name="Contact"),
    #Datos Personales
    path('datos_personales',datos_personales,name="DatosPersonales"),
    path('agregarAvatar',agregarAvatar,name="AgregarAvatar"),
    path('perfil',perfil,name="Perfil"), #Perfil Muestra el Curriculo del usuario
    path('perfilde/<str:nombre>', perfilde, name='unperfil'),
    #Skill
    path('skill/', SkillListView.as_view(), name='skill_list'),
    path('skill/crear/', SkillCreateView.as_view(), name='skill_create'),
    path('skill/<int:pk>/', SkillDetailView.as_view(), name='skill_detalle'),
    path('skill/editar/<int:pk>/', SkillUpdateView.as_view(), name='skill_update'),
    path('skill/eliminar/<int:pk>/', SkillDeleteView.as_view(), name='skill_delete'),
    #Idiomas
    path('idioma/', IdiomaListView.as_view(), name='idioma_list'),
    path('idioma/crear/', IdiomaCreateView.as_view(), name='idioma_create'),
    path('idioma/<int:pk>/', IdiomaDetailView.as_view(), name='idioma_detalle'),
    path('idioma/editar/<int:pk>/', IdiomaUpdateView.as_view(), name='idioma_update'),
    path('idioma/eliminar/<int:pk>/', IdiomaDeleteView.as_view(), name='idioma_delete'),
    #Educacion
    path('educacion',estudio,name="Educacion"),
    path('educacion/',estudio,name="EducacionSearch"),
    path('eliminareducacion/<str:id>', eliminar_educacion, name='EliminaEducacion'),
    path('editareducacion/<str:id>', editar_educacion, name='EditaEducacion'),
    #Experiencia
    path('experiencia',experiencia,name="Experiencia"),
    path('experiencia/',experiencia,name="ExperienciaSearch"),
    path('eliminarexperiencia/<str:id>', eliminar_experiencia, name='EliminaExperiencia'),
    path('editarexperiencia/<str:id>', editar_experiencia, name='EditaExperiencia'),
    #Publicaciones
    path('publicaciones',publicacion,name="Publicaciones"),
    path('publicaciones/',publicacion,name="PublicacionSearch"),
    path('eliminarpublicacion/<str:id>', eliminar_publicacion, name='EliminaPublicacion'),
    path('editarpublicacion/<str:id>', editar_publicacion, name='EditaPublicacion'),
    #Noticias: Es una lista de las publicaciones de los usuarios
    path('noticias',noticias,name="Noticias"),
    path('noticias/',noticias,name="NoticiasSearch"),

]
