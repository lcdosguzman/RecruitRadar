from django.urls import path
from appUsers import views

urlpatterns = [
    path('',views.home,name="Home"),
]