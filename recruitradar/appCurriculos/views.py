from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,"appCurriculos/home.html")

def admin_home(request):
    return render(request,"appCurriculos/admin_home.html")

def otrapp(request):
    return render(request,"appCurriculos/otrapp.html",{"avatar":request.session.get('foto-avatar', 'none')})