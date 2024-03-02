from django.urls import path
from appUsers import views

urlpatterns = [
    path('',views.home,name="Home"),
    path('login',views.login,name="Login"),
    path('registro',views.registro,name="Registro"),
    path('aboutme',views.aboutme,name="Aboutme"),
    path('contact',views.contact,name="Contact"),
]