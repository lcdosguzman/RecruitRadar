from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.models import User
from .models import Avatar
  
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir Contraseña",widget=forms.PasswordInput)
    last_name = forms.CharField(label='Nombre', max_length=100,widget=forms.TextInput)
    first_name = forms.CharField(label='Apellido', max_length=100,widget=forms.TextInput)

    class Meta:
        model = User
        fields = ['username','email','password1','password2','last_name','first_name']

class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']  # Lista de campos que deseas incluir en el formulario

    def __init__(self, *args, **kwargs):
        super(AvatarFormulario, self).__init__(*args, **kwargs)
        # Personaliza los widgets o agrega clases CSS si es necesario
        self.fields['imagen'].widget.attrs.update({'class': 'form-control-file'})


class DataUsuarioFormulario(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellido = forms.CharField(label='Apellido', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(label='Biografía', max_length=1000,widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(label='Teléfono', max_length=20,widget=forms.TextInput(attrs={'class': 'form-control'}))
    url_facebook = forms.CharField(label='URL facebook', max_length=80,widget=forms.TextInput(attrs={'class': 'form-control'}))
    url_twitter = forms.CharField(label='URL twitter', max_length=80,widget=forms.TextInput(attrs={'class': 'form-control'}))
    url_github = forms.CharField(label='URL github', max_length=80,widget=forms.TextInput(attrs={'class': 'form-control'}))
    url_youtube = forms.CharField(label='URL youtube', max_length=80,widget=forms.TextInput(attrs={'class': 'form-control'}))
    url_linkedin = forms.CharField(label='URL linkedin', max_length=80,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej: https://linkedin.com/sromero'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'Nombre',
            'apellido',
            'biografía',
            'telefono',
            'url_facebook',
            'url_twitter',
            'url_github',
            'url_youtube',
            'url_linkedin',
            Submit('submit', 'Guardar', css_class='btn btn-primary')
        )

class PublicacionFormulario(forms.Form):
    titulo = forms.CharField(label='Titulo', max_length=1000,widget=forms.TextInput(attrs={'class': 'form-control'}))
    contenido = forms.CharField(label='Contenido', max_length=1000,widget=forms.TextInput(attrs={'class': 'form-control'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'Titulo',
            'Contenido',
            Submit('submit', 'Guardar', css_class='btn btn-primary')
        )
class SkillFormulario(forms.Form):
    aptitud = forms.CharField(label='Aptitud', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej: Github'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'aptitud',
            Submit('submit', 'Guardar', css_class='btn btn-primary')
        )

class IdiomaFormulario(forms.Form):
    idioma = forms.CharField(label='Idioma', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej: Portugues'}))
    nivel = forms.CharField(label='Nivel', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej: Basico'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'idioma',
            'nivel',
            Submit('submit', 'Guardar', css_class='btn btn-primary')
        )

class ExperienciaFormulario(forms.Form):
    cargo = forms.CharField(label='Cargo', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej: Programador Backend Ssr'}))
    empresa = forms.CharField(label='Empresa', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'La Compañia S.A.'}))
    description = forms.CharField(label='Description', max_length=1000,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej: Indique descripción del cargo'}))
    pais = forms.CharField(label='Pais', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej: Venezuela'}))
    periodo_inicio = forms.IntegerField(label='Fecha Inicio',widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej: 2003'}))
    periodo_fin = forms.IntegerField(label='Fecha Fin',widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej: 2013'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'cargo',
            'empresa',
            'description',
            'pais',
            'fecha_inicio',
            'fecha_fin',
            Submit('submit', 'Guardar', css_class='btn btn-primary')
        )

class EstudioFormulario(forms.Form):
    institucion = forms.CharField(label='Institucion', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej: Universidad de Buenos Aires'}))
    titulo = forms.CharField(label='Titulo', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej: Licenciado en Informática'}))
    description = forms.CharField(label='Description', max_length=1000,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej: Indique una descripción del estudio realizado'}))
    pais = forms.CharField(label='Pais', max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Argentina'}))
    periodo_inicio = forms.IntegerField(label='Fecha Inicio',widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej: 2005'}))
    periodo_fin = forms.IntegerField(label='Fecha Fin',widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej: 2013'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'institucion',
            'titulo',
            'description',
            'pais',
            'fecha_inicio',
            'fecha_fin',
            Submit('submit', 'Guardar', css_class='btn btn-primary')
        )