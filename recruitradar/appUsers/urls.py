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
]