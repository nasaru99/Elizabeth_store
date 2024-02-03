from django.contrib import admin
from .models import (Rol, Usuario, Categoria, Proveedor, Producto, ImagenProducto,
                     Cliente, Trabajador, Encargo, Caja, TipoTransferencia, Venta,
                     ImagenTransferencia, DetalleVenta, Credito, HistorialCaja)

# Registro simple de modelos
admin.site.register(Rol)
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(ImagenProducto)
admin.site.register(TipoTransferencia)
admin.site.register(ImagenTransferencia)

# Registro personalizado con decorador para mostrar más detalles en la interfaz de administración
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_usuario', 'correo', 'rol')
    search_fields = ('nombre_usuario', 'correo')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'existencia', 'precio', 'categoria', 'proveedor')
    list_filter = ('categoria', 'proveedor')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'usuario')
    search_fields = ('nombre', 'usuario__nombre_usuario')

@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('nombre_trabajador', 'fecha_ingreso', 'telefono')

@admin.register(Encargo)
class EncargoAdmin(admin.ModelAdmin):
    list_display = ('trabajador', 'producto', 'fecha', 'estado')
    list_filter = ('fecha', 'estado')

@admin.register(Caja)
class CajaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad_inicial', 'cantidad_final', 'estado', 'trabajador')

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'total_venta', 'cliente', 'trabajador', 'caja')
    list_filter = ('fecha', 'cliente', 'trabajador')

@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('venta', 'producto', 'cantidad_producto', 'precio', 'total')

@admin.register(Credito)
class CreditoAdmin(admin.ModelAdmin):
    list_display = ('venta', 'abono', 'cantidad_abonos', 'saldo_deuda')

@admin.register(HistorialCaja)
class HistorialCajaAdmin(admin.ModelAdmin):
    list_display = ('caja', 'fecha', 'cantidad_inicial', 'cantidad_final', 'trabajador')
    list_filter = ('fecha', 'trabajador')
