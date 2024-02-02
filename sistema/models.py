from django.db import models
from django.contrib.auth.models import User

class Rol(models.Model):
    nombre = models.CharField(max_length=255)

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=255)
    contraseña = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

class Proveedor(models.Model):
    nombre = models.CharField(max_length=255)
    telefono = models.IntegerField()
    descripcion = models.TextField()

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    existencia = models.IntegerField()
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

class ImagenProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    telefono = models.IntegerField()
    descripcion = models.TextField()
    estado = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Trabajador(models.Model):
    nombre_trabajador = models.CharField(max_length=255)
    fecha_ingreso = models.DateTimeField()
    telefono = models.IntegerField()

class Encargo(models.Model):
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    estado = models.CharField(max_length=255)

class Caja(models.Model):
    nombre = models.CharField(max_length=255)
    cantidad_inicial = models.IntegerField()
    cantidad_final = models.IntegerField()
    estado = models.IntegerField()
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)

class TipoTransferencia(models.Model):
    nombre = models.CharField(max_length=255)
    estado = models.IntegerField()

class Venta(models.Model):
    total_venta = models.IntegerField()
    fecha = models.DateTimeField()
    venta_credito = models.IntegerField()
    transferencia = models.ForeignKey(TipoTransferencia, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    caja = models.ForeignKey(Caja, on_delete=models.CASCADE)

class ImagenTransferencia(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_producto = models.IntegerField()
    precio = models.IntegerField()
    total = models.IntegerField()

class Credito(models.Model):
    abono = models.IntegerField()
    cantidad_abonos = models.IntegerField()
    saldo_deuda = models.IntegerField()
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)

class HistorialCaja(models.Model):
    caja = models.ForeignKey(Caja, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    cantidad_inicial = models.IntegerField()
    cantidad_final = models.IntegerField()
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
