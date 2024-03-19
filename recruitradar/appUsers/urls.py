from django.urls import path
from appUsers import views
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
#url
urlpatterns = [
    path('',views.home,name="Home"),
    path('login',views.login_request,name="Login"),
    path('logout',views.logout_request,name="Logout"),
    path('register',views.register,name="Register"),
    path('registro',views.registro,name="Registro"),
    path('editarusuario',views.editar_usuario,name="EditarUsuario"),
    path('aboutme',views.aboutme,name="Aboutme"),
    path('contact',views.contact,name="Contact"),

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
    path('editarpublicacion/<str:id>', views.editar_publicacion, name='EditaPublicacion'),

    path('experiencia',views.experiencia,name="Experiencia"),
    path('experiencia/',views.experiencia,name="Experiencia"),
    path('eliminarexperiencia/<str:id>', views.eliminar_experiencia, name='EliminaExperiencia'),
    path('editarexperiencia/<str:id>', views.editar_experiencia, name='EditaExperiencia'),

    path('educacion',views.estudio,name="Educacion"),
    path('educacion/',views.estudio,name="Educacion"),
    path('eliminareducacion/<str:id>', views.eliminar_educacion, name='EliminaEducacion'),
    path('editareducacion/<str:id>', views.editar_educacion, name='EditaEducacion'),

    path('perfil',views.perfil,name="Perfil"),
    path('agregarAvatar',views.agregarAvatar,name="AgregarAvatar"),
    path('perfilde/<str:nombre>', views.perfilde, name='unperfil'),
    
    path('idioma/', views.IdiomaListView.as_view(), name='idioma_list'),
    path('idioma/crear/', views.IdiomaCreateView.as_view(), name='idioma_create'),
    path('idioma/<int:pk>/', views.IdiomaDetailView.as_view(), name='idioma_detalle'),
    path('idioma/editar/<int:pk>/', views.IdiomaUpdateView.as_view(), name='idioma_update'),
    path('idioma/eliminar/<int:pk>/', views.IdiomaDeleteView.as_view(), name='idioma_delete'),

    path('skill/', views.SkillListView.as_view(), name='skill_list'),
    path('skill/crear/', views.SkillCreateView.as_view(), name='skill_create'),
    path('skill/<int:pk>/', views.SkillDetailView.as_view(), name='skill_detalle'),
    path('skill/editar/<int:pk>/', views.SkillUpdateView.as_view(), name='skill_update'),
    path('skill/eliminar/<int:pk>/', views.SkillDeleteView.as_view(), name='skill_delete'),
    
]
'''
path('idioma/list', views.IdiomaList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.IdiomaDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.IdiomaCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.IdiomaUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.IdiomaDelete.as_view(), name='Delete'),
'''