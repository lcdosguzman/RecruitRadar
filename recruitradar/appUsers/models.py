from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class DataUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.CharField(max_length=1000, null=True, blank = True)
    telefono = models.CharField(max_length=100, null=True, blank = True)
    url_twitter = models.CharField(max_length=100,null=True, blank = True)
    url_facebook = models.CharField(max_length=100, null=True, blank = True)
    url_github= models.CharField(max_length=100, null=True, blank = True)
    url_youtube = models.CharField(max_length=100, null=True, blank = True)
    url_linkedin = models.CharField(max_length=100, null=True, blank = True)

    def __str__(self):
        return self.bio
    
class Publicacion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=100, null=True, blank = True)
    contenido = models.CharField(max_length=1000, null=True, blank = True)
    def __str__(self):
        return self.titulo
    
class Skills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    aptitud = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.aptitud}'
    
class Idiomas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    idioma = models.CharField(max_length=50)
    nivel = models.CharField(max_length=20) 

    def __str__(self):
        return f'{self.idioma} - Nivel: {self.nivel}'
    
class ExperienciaLaboral(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cargo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    periodo_inicio = models.IntegerField()
    periodo_fin = models.IntegerField(null=True, blank=True) 
    description = models.CharField(max_length=1000)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.cargo} en {self.empresa}'

class Educacion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    institucion = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    pais = models.CharField(max_length=50)
    periodo_inicio = models.IntegerField()
    periodo_fin = models.IntegerField(null=True, blank=True) 

    def __str__(self):
        return f'{self.titulo} en {self.institucion}'