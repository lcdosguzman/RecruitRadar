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
]
