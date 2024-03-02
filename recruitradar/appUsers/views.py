from django.shortcuts import render
from django.http import HttpResponse
from appUsers.models import *

# Create your views here.
def home(request):
    return render(request,"appUsers/home.html")