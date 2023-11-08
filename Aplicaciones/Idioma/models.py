from django.db import models
from Aplicaciones.Pais.models import Pais

# Create your models here.
class Idioma (models.Model):
    Nombre = models.CharField('Idioma', max_length=60)
    Codigo = models.CharField('Codigo de Idioma', max_length=2)
    Descripcion = models.CharField('Descripcion del Idioma', max_length=255)
    Pais = models.ManyToManyField(Pais)


    class Meta:
        verbose_name = 'Idioma'
        verbose_name_plural = 'Idiomas'
        ordering = ['Nombre']

    def __str__(self) -> str:
        return str(self.id)+' -- '+self.Nombre+' -- '+self.Codigo+' -- '+self.Descripcion
