from django.shortcuts import render
from django.http import HttpResponse
from appUsers.models import *

# Create your views here.
def home(request):
    return render(request,"appUsers/home.html")

def login(request):
    return render(request,"appUsers/login.html")

def registro(request):
    return render(request,"appUsers/registro.html")

def aboutme(request):
    return render(request,"appUsers/aboutme.html")

def contact(request):
    return render(request,"appUsers/contact.html")