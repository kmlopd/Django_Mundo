from django.db import models

# Create your models here.
class Continente (models.Model):
    Nombre = models.CharField('Nombre del Continente', max_length=30)
    Extencion = models.CharField('Extension del Continente', max_length=20)

    class Meta:
        verbose_name = 'Continente'
        verbose_name_plural = 'Continentes'
        ordering = ['Nombre']

    def __str__(self) -> str:
        return str(self.id)+' -- '+self.Nombre+' -- '+self.Extencion