from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(TipoPago)
admin.site.register(Comuna)
admin.site.register(Region)
admin.site.register(Invitado)
admin.site.register(Sucursal)
admin.site.register(Orden)
admin.site.register(Detalle_orden)
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombreCategoria',)}
    list_display = ('nombreCategoria', 'slug')

admin.site.register(Categoria,CategoriaAdmin)

class SubCategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombreSubCategoria',)}
    list_display = ('nombreSubCategoria', 'slug')

admin.site.register(SubCategoria,SubCategoriaAdmin)

class TipoInstrumentoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombreTipoInstrumento',)}
    list_display = ('nombreTipoInstrumento', 'slug')

admin.site.register(TipoInstrumento,TipoInstrumentoAdmin)

class MarcaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombreMarca',)}
    list_display = ('nombreMarca', 'slug')

admin.site.register(Marca, MarcaAdmin)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombreProducto', 'precio', 'stock', 'modified_date')
    prepopulated_fields = {'slug': ('nombreProducto',)}


admin.site.register(Producto,ProductoAdmin)

