from asyncio.windows_events import NULL
from distutils.command.upload import upload
from tkinter.tix import INCREASING
from django.db import models
from django.forms import EmailField

# Create your models here.
# validamos que no permita valores nulos ni en blanco--> null=False, blank=False
class Usuario (models.Model):
        id_usuario = models.IntegerField(primary_key = True)
        nombre = models.CharField(max_length=15, null=False, blank=False)
        apellidoPaterno = models.CharField(max_length=10)
        apellidoMaterno = models.CharField(max_length=10, null=False, blank=False)
        email = models.EmailField(max_length=254, null=False, blank=False)
        contraseña = models.CharField(max_length=10, null=False, blank=False)
        telefono = models.IntegerField(null=False, blank=False)
        direccion = models.CharField(max_length=500, null=False, blank=False)
        comuna = models.CharField(max_length=15, null=False, blank=False)
        region = models.CharField(max_length=15, null=False, blank=False)

        
        def __str__(self):
                return self.nombre

class TipoUser (models.Model):
        id_tipoUser =  models.IntegerField(primary_key = True)
        tipoUser = models.CharField(max_length=15, null=False, blank=False)
        id_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)

        
        def __str__(self):
                return self.tipoUser

class Categoria (models.Model):
        id_categoria = models.IntegerField(primary_key = True)
        descripcion = models.CharField(max_length=30)

        def __str__(self):
                return self.descripcion

class Producto (models.Model):
        id_producto = models.IntegerField(primary_key = True)
        nombre = models.CharField(max_length=15)
        stock = models.IntegerField()
        precio = models.IntegerField()
        id_categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

        def __str__(self):
                return f'{self.nombre} -> {self.precio}'

class Descuento (models.Model):
        id_desucento = models.IntegerField(primary_key = True)
        promocion = models.BooleanField 
        subscripcion = models.BooleanField

        def __str__(self):
                return self.promocion

class Venta (models.Model):
        id_venta = models.IntegerField(primary_key = True)
        fecha = models.DateField
        descripcion = models.CharField(max_length=200)
        total_vent = models.IntegerField()
        id_descuento = models.ForeignKey(Descuento, on_delete=models.PROTECT)
        id_producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
        id_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
        id_categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)


        def __str__(self):
                return self.descripcion

class Carrito (models.Model):
        id_carrito = models.IntegerField(primary_key = True)
        id_producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
        id_venta = models.ForeignKey(Venta, on_delete=models.PROTECT)
        id_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
        
        def __str__(self):
                return self.id_carrito

class Despacho (models.Model):
        id_despacho = models.IntegerField(primary_key = True)
        fecha = models.DateField
        descripcion = models.CharField(max_length=200)
        direccion = models.CharField(max_length=50)
        id_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
        id_venta = models.ForeignKey(Venta, on_delete=models.PROTECT)

        def __str__(self):
                return self.descripcion

class Estado_despacho (models.Model):
        id_estado_despacho = models.IntegerField(primary_key = True)
        descripcion = models.CharField(max_length=30)
        id_despacho = models.ForeignKey(Despacho, on_delete=models.PROTECT)
        
        def __str__(self):
                return self.descripcion

