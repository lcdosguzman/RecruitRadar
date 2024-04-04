from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from appUsers.models import *
from appUsers.forms import *
from appCurriculos.models import *
from appCurriculos.forms import *

@login_required
def eliminar_experiencia(request,id):
    try:
        data = ExperienciaLaboral.objects.get(id=id)
        data.delete()
    except ExperienciaLaboral.DoesNotExist:
          return redirect('Experiencia')
    
    data = ExperienciaLaboral.objects.filter(user=request.user)
    return redirect('Experiencia')

@login_required
def editar_experiencia(request,id):
    resp=""
    data= ExperienciaLaboral.objects.get(id=id)
    if request.method == 'POST':
        form = ExperienciaFormulario(request.POST)
        if form.is_valid():
            dataf = form.cleaned_data
            data.empresa=dataf['empresa']
            data.cargo=dataf['cargo']
            data.description=dataf['description']
            data.pais=dataf['pais']
            data.periodo_inicio=dataf['periodo_inicio']
            data.periodo_fin=dataf['periodo_fin']
            data.save()
            exp = ExperienciaLaboral.objects.filter(user=request.user)
            miFormulario = ExperienciaFormulario()
            return redirect('Experiencia')
        else:
            resp="datos no validos"
            form = ExperienciaFormulario(initial={'empresa':data.empresa,'cargo':data.cargo,'description':data.description,'pais':data.pais,'periodo_inicio':data.periodo_inicio,'periodo_fin':data.periodo_fin})
            return render(request,"appCurriculos/editarexperiencia.html",{"resp":resp,"form":form,"avatar":request.session.get('foto-avatar', 'none')})
    
    form = ExperienciaFormulario(initial={'empresa':data.empresa,'cargo':data.cargo,'description':data.description,'pais':data.pais,'periodo_inicio':data.periodo_inicio,'periodo_fin':data.periodo_fin})      
    return render(request,"appCurriculos/editarexperiencia.html",{"resp":resp,"form":form,"avatar":request.session.get('foto-avatar', 'none')})

@login_required
def experiencia(request):
    experiencias = ExperienciaLaboral.objects.filter(user=request.user)
    if request.method == 'POST':
        miFormulario = ExperienciaFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            if 'periodo_inicio'in request.POST:
                u = User.objects.get(username = request.user)
                informacion = miFormulario.cleaned_data
                exp = ExperienciaLaboral (user=u,cargo=informacion['cargo'],empresa=informacion['empresa'],periodo_fin=informacion['periodo_fin'],periodo_inicio=informacion['periodo_inicio'],description=informacion['description'],pais=informacion['pais'])
                exp.save()
                miFormulario = ExperienciaFormulario()
                return render(request,"appCurriculos/experiencia.html",{"experiencias":experiencias,"miFormulario":miFormulario,"resp":"Datos guardados Correctamente","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})
            else:
                return render(request,"appCurriculos/experiencia.html",{"experiencias":experiencias,"miFormulario":miFormulario,"resp":"Datos No Guardados","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})
    else:
        miFormulario = ExperienciaFormulario()
    
    if 'text_search' in request.GET:
        search = request.GET['text_search']
        experienciaSearch = ExperienciaLaboral.objects.filter(description__icontains=search,user=request.user)
        respSearch = "No se encontraron resultados para " + search
        if experienciaSearch.exists():
            respSearch = "Resultados para " + search
        return render(request,"appCurriculos/experiencia.html",{"experiencias":experiencias,"miFormulario":miFormulario,"experienciaSearch":experienciaSearch,"resp":"","respSearch":respSearch,"avatar":request.session.get('foto-avatar', 'none')})

    return render(request,"appCurriculos/experiencia.html",{"experiencias":experiencias,"miFormulario":miFormulario,"resp":"","respSearch":"","avatar":request.session.get('foto-avatar', 'none')})
