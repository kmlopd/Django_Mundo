from django.contrib import admin
from .models import Ciudad


class CiudadAdmin (admin.ModelAdmin):
    list_display = (
        'Nombre',
        'Codigo',
    )

    search_fields = ('Nombre','')
    list_filter = ('Pais',)


# Register your models here.
admin.site.register(Ciudad,CiudadAdmin)