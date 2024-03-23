from django.urls import path
from appUsers import views
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
#url
urlpatterns = [
    path('login',views.login_request,name="Login"),
    path('logout',views.logout_request,name="Logout"),
    path('register',views.register,name="Register"),
    path('editarusuario',views.editar_usuario,name="EditarUsuario"),
]
