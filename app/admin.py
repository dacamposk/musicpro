from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Comuna)
admin.site.register(Region)
admin.site.register(Invitado)
admin.site.register(Sucursal)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombreCategoria', 'slug')

admin.site.register(Categoria, CategoriaAdmin)

class SubCategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombreSubCategoria', 'slug')

admin.site.register(SubCategoria, SubCategoriaAdmin)

class TipoInstrumentoAdmin(admin.ModelAdmin):
    list_display = ('nombreTipoInstrumento', 'slug')

admin.site.register(TipoInstrumento, TipoInstrumentoAdmin)

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombreMarca', 'slug')

admin.site.register(Marca, MarcaAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombreProducto', 'precio', 'stock', 'modified_date')

admin.site.register(Producto, ProductoAdmin)
admin.site.register(UserUbicacion)