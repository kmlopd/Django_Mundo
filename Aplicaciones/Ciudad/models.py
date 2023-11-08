from django.db import models
from Aplicaciones.Pais.models import Pais

# Create your models here.
class Ciudad (models.Model):
    Nombre = models.CharField('Nombre de la Ciudad', max_length=60)
    Codigo = models.CharField('Codigo de la Ciudad', max_length=3)
    Pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        ordering = ['Nombre']

    def __str__(self) -> str:
        return str(self.id)+' -- '+self.Nombre+' -- '+self.Codigo+' -- '+str(self.Pais)
