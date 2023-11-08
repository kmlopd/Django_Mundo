from django.contrib import admin
from .models import Continente

class ContinenteAdmin (admin.ModelAdmin):
    list_display = (
        'Nombre',
        'Extencion',
    )

    search_fields = ('Nombre','')

# Register your models here.
admin.site.register(Continente,ContinenteAdmin)

