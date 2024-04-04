from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from appUsers.models import *
from appUsers.forms import *
from appCurriculos.models import *
from appCurriculos.forms import *

@login_required
def editar_educacion(request,id):
    resp=""
    data= Educacion.objects.get(id=id)
    if request.method == 'POST':
        form = EstudioFormulario(request.POST)
        if form.is_valid():
            dataf = form.cleaned_data
            data.institucion=dataf['institucion']
            data.titulo=dataf['titulo']
            data.description=dataf['description']
            data.pais=dataf['pais']
            data.periodo_inicio=dataf['periodo_inicio']
            data.periodo_fin=dataf['periodo_fin']
            data.save()
            estudios = Educacion.objects.filter(user=request.user)
            miFormulario = EstudioFormulario()
            return redirect('Educacion')
        else:
            resp="datos no validos"
            form = EstudioFormulario(initial={'institucion':data.institucion,'titulo':data.titulo,'description':data.description,'pais':data.pais,'periodo_inicio':data.periodo_inicio,'periodo_fin':data.periodo_fin})
            return render(request,"appCurriculos/editareducacion.html",{"resp":resp,"form":form,"avatar":request.session.get('foto-avatar', 'none')})
    
    form = EstudioFormulario(initial={'institucion':data.institucion,'titulo':data.titulo,'description':data.description,'pais':data.pais,'periodo_inicio':data.periodo_inicio,'periodo_fin':data.periodo_fin})      
    return render(request,"appCurriculos/editareducacion.html",{"resp":resp,"form":form,"avatar":request.session.get('foto-avatar', 'none')})

@login_required
def eliminar_educacion(request,id):
    try:
        data = Educacion.objects.get(id=id)
        data.delete()
    except Educacion.DoesNotExist:
          return redirect('Educacion')
    
    data = Educacion.objects.filter(user=request.user)
    return redirect('Educacion')

@login_required
def estudio(request):

    estudios = Educacion.objects.filter(user=request.user)
    if request.method == 'POST':
        miFormulario = EstudioFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
                u = User.objects.get(username = request.user)
                informacion = miFormulario.cleaned_data
                exp = Educacion(user=u,institucion=informacion['institucion'],titulo=informacion['titulo'],periodo_fin=int(informacion['periodo_fin']),periodo_inicio=int(informacion['periodo_inicio']),description=informacion['description'],pais=informacion['pais'])
                exp.save()
                miFormulario = EstudioFormulario()
                return render(request,"appCurriculos/educacion.html",{"estudios":estudios,"miFormulario":miFormulario,"resp":"Datos guardados Correctamente","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})
        else:
          return render(request,"appCurriculos/educacion.html",{"estudios":estudios,"miFormulario":miFormulario,"resp":"Datos no guardados Correctamente","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})
    else:
        miFormulario = EstudioFormulario()

    if 'text_search' in request.GET:
        search = request.GET['text_search']
        estudiosSearch = Educacion.objects.filter(description__icontains=search,user=request.user)
        respSearch = "No se encontraron resultados para " + search
        if estudiosSearch.exists():
            respSearch = "Resultados para " + search
        return render(request,"appCurriculos/educacion.html",{"estudios":estudios,"miFormulario":miFormulario,"estudiosSearch":estudiosSearch,"resp":"","respSearch":respSearch,"avatar":request.session.get('foto-avatar', 'none')})

    return render(request,"appCurriculos/educacion.html",{"estudios":estudios,"miFormulario":miFormulario,"resp":"","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})
