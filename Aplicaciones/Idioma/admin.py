from django.contrib import admin
from .models import Idioma

class IdiomaAdmin (admin.ModelAdmin):
    list_display = (
        'Nombre',
        'Codigo',
        'Descripcion',
    )

    search_fields = ('Nombre','')
    # list_filter = ('Tipo','Continente')
    filter_horizontal = ('Pais',)

# Register your models here.
admin.site.register(Idioma,IdiomaAdmin)