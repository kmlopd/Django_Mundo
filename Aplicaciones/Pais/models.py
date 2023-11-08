from django.db import models
from Aplicaciones.Continente.models import Continente

# Create your models here.
class Pais (models.Model):
    Tipo_Choices = (
        ('1', 'Desarrollado'),
        ('2', 'Sub-Desarrollado'),
    )

    Nombre = models.CharField('Nombre del Pais', max_length=60)
    Codigo = models.CharField('Codigo del Pais', max_length=3)
    Poblacion = models.IntegerField('N° Poblacion del Pais', default=1)
    Tipo = models.CharField('Tipo de Pais', max_length=1, choices=Tipo_Choices)
    Continente = models.ManyToManyField(Continente)

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
        ordering = ['Nombre']


    def __str__(self) -> str:
        return str(self.id)+' -- '+self.Nombre+' -- '+self.Codigo+' -- '+str(self.Poblacion)+' Millones -- '+self.Tipo