from django.contrib import admin
from .models import Usuario, TipoUser, Producto, Categoria,  Venta, Despacho, Estado_despacho, Descuento, Carrito, Historial
# Register your models here.

# Register your models here.
admin.site.register(Usuario)
admin.site.register(TipoUser)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Venta)
admin.site.register(Despacho)
admin.site.register(Estado_despacho)
admin.site.register(Descuento)
admin.site.register(Carrito)

