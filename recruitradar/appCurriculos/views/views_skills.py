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

class SkillListView(LoginRequiredMixin, ListView):
    model = Skills
    template_name = 'appCurriculos/skill_list.html'
    context_object_name = 'skills'
    def get_queryset(self):
        return Skills.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar'] = self.request.session.get('foto-avatar', 'none')
        return context

class SkillCreateView(LoginRequiredMixin, CreateView):
    model = Skills
    template_name = 'appCurriculos/skill_form.html'
    fields = ['aptitud']
    success_url = reverse_lazy('skill_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar'] = self.request.session.get('foto-avatar', 'none')
        return context

class SkillUpdateView(LoginRequiredMixin, UpdateView):
    model = Skills
    template_name = 'appCurriculos/skill_form.html'
    fields = ['aptitud']
    success_url = reverse_lazy('skill_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar'] = self.request.session.get('foto-avatar', 'none')
        return context

class SkillDeleteView(LoginRequiredMixin, DeleteView):
    model = Skills
    template_name = 'appCurriculos/skill_confirm_delete.html'
    success_url = reverse_lazy('skill_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar'] = self.request.session.get('foto-avatar', 'none')
        context['skill'] = self.get_object()  # Asegúrate de que 'idioma' sea el nombre de tu objeto en la plantilla
        return context
    
class SkillDetailView(LoginRequiredMixin,DetailView):
    model = Skills
    template_name = 'appCurriculos/skill_detalle.html'
    context_object_name = 'skill'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar'] = self.request.session.get('foto-avatar', 'none')
        return context