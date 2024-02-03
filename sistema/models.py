from django.db import models
#from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
#from django.utils import timezone
# class UsuarioManager(BaseUserManager):
#     def create_user(self, correo, password, **extra_fields):
#         if not correo:
#             raise ValueError('El correo es obligatorio')
#         usuario = self.model(correo=self.normalize_email(correo), **extra_fields)
#         usuario.set_password(password)
#         usuario.save(using=self._db)
#         return usuario

#     def create_superuser(self, correo, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(correo, password, **extra_fields)

class Rol(models.Model):
    nombre = models.CharField(max_length=255)

# class Usuario(AbstractBaseUser, PermissionsMixin):
#     nombre_usuario = models.CharField(max_length=255, null=True)
#     password = models.CharField(max_length=255, )
#     correo = models.EmailField(unique=True)
#     rol = models.ForeignKey(Rol, on_delete=models.CASCADE, null=True, blank=True)
#     is_staff = models.BooleanField(default=False)  # Agregado
#     is_active = models.BooleanField(default=True)  # Agregado
#     date_joined = models.DateTimeField(default=timezone.now)  # Agregado

#     objects = UsuarioManager()

#     USERNAME_FIELD = 'correo'
#     REQUIRED_FIELDS = ['nombre_usuario']

#     def __str__(self):
#         return self.correo
    
class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=255)
    contraseña = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

class Categoria(models.Model):
    GENEROS = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('U', 'Unisex'),
        ('N', 'No Especificado'),  # Opcional, dependiendo de tus necesidades
    ]

    nombre = models.CharField(max_length=255)
    genero = models.CharField(max_length=1, choices=GENEROS, default='N')  # Añade el campo genero

class Proveedor(models.Model):
    nombre = models.CharField(max_length=255)
    telefono = models.IntegerField()
    descripcion = models.TextField()

class Talla(models.Model):
    nombre = models.CharField(max_length=10)  # Longitud ajustada para nombres de talla más largos
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='tallas')

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    existencia = models.IntegerField()
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    talla = models.ForeignKey(Talla, on_delete=models.CASCADE, related_name='productos')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

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
