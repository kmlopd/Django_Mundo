from django.contrib import admin
from .models import Pais

# Register your models here.
class PaisAdmin (admin.ModelAdmin):
    list_display = (
        'Nombre',
        'Poblacion',
        'Tipo',
    )

    search_fields = ('Nombre','')
    list_filter = ('Tipo','Continente')
    filter_horizontal = ('Continente',)


admin.site.register(Pais,PaisAdmin)