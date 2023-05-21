from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Invitado)
admin.site.register(Categoria)
admin.site.register(SubCategoria)
admin.site.register(TipoInstrumento)
admin.site.register(Marca)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'modified_date')


admin.site.register(Producto,ProductoAdmin)