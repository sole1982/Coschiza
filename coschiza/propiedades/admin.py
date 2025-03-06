from django.contrib import admin
from .models import Propiedad, ImagenPropiedad


@admin.register(Propiedad)
class PropiedadAdmin(admin.ModelAdmin):
   class PropiedadAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo_propiedad', 'estado_publicacion', 'localidad', 'provincia', 'precio')
    search_fields = ('titulo', 'direccion', 'localidad', 'provincia')
    list_filter = ('tipo_propiedad', 'estado_publicacion', 'provincia', 'localidad')
    ordering = ('titulo',)

class ImagenPropiedadAdmin(admin.ModelAdmin):
    list_display = ('propiedad', 'imagen')

admin.site.register(ImagenPropiedad, ImagenPropiedadAdmin)
   