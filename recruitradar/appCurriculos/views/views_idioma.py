from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from appUsers.models import *
from appUsers.forms import *
from appCurriculos.models import *
from appCurriculos.forms import *

class IdiomaListView(LoginRequiredMixin, ListView):
    model = Idiomas
    template_name = 'appCurriculos/idiomas_list.html'
    context_object_name = 'idiomas'
    def get_queryset(self):
        return Idiomas.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar'] = self.request.session.get('foto-avatar', 'none')
        return context

class IdiomaCreateView(LoginRequiredMixin, CreateView):
    model = Idiomas
    template_name = 'appCurriculos/idiomas_form.html'
    fields = ['idioma', 'nivel']
    success_url = reverse_lazy('idioma_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar'] = self.request.session.get('foto-avatar', 'none')
        return context

class IdiomaUpdateView(LoginRequiredMixin, UpdateView):
    model = Idiomas
    template_name = 'appCurriculos/idiomas_form.html'
    fields = ['idioma', 'nivel']
    success_url = reverse_lazy('idioma_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar'] = self.request.session.get('foto-avatar', 'none')
        return context

class IdiomaDeleteView(LoginRequiredMixin, DeleteView):
    model = Idiomas
    template_name = 'appCurriculos/idiomas_confirm_delete.html'
    success_url = reverse_lazy('idioma_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar'] = self.request.session.get('foto-avatar', 'none')
        context['idioma'] = self.get_object()  # Asegúrate de que 'idioma' sea el nombre de tu objeto en la plantilla
        return context
    
class IdiomaDetailView(LoginRequiredMixin,DetailView):
    model = Idiomas
    template_name = 'appCurriculos/idiomas_detalle.html'
    context_object_name = 'idioma'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar'] = self.request.session.get('foto-avatar', 'none')
        return context

class IdiomaList(ListView):
    model = Idiomas
    template_name = "appCurriculos/idiomas_list.html"  