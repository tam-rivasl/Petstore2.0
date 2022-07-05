from django.db import models
from django.forms import EmailField

# Create your models here.

class Usuario (models.Model):
        id_usuario = models.IntegerField(primary_key = True, max_length=3)
        nombre = models.CharField(max_length=15)
        apellidoPaterno = models.CharField(max_length=10)
        apellidoMaterno = models.CharField(max_length=10)
        email = EmailField()
        contraseña = models.CharField(max_length=10)
        telefono = models.IntegerField(max_length=9)
        direccion = models.IntegerField(max_length=10)
        comuna = models.CharField(max_length=15)
        region = models.CharField(max_length=15)

class TipoUser (models.Model):
        id_tipoUser =  models.IntegerField(primary_key = True, max_length=3)
        tipoUser = models.IntegerField(max_length=30)
        id_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)

class Categoria (models.Model):
        id_categoria = models.IntegerField(primary_key = True, max_length=1)
        descripcion = models.CharField(max_length=30)


class Producto (models.Model):
        id_producto = models.IntegerField(primary_key = True, max_length=10)
        nombre = models.CharField(max_length=15)
        stock = models.IntegerField(max_length=3)
        precio = models.IntegerField(max_length=6)
        id_categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)


class Descuento (models.Model):
        id_desucento = models.IntegerField(primary_key = True, max_length=7)
        promocion = models.BooleanField 
        subscripcion = models.BooleanField

class Venta (models.Model):
        id_venta = models.IntegerField(primary_key = True, max_length=7)
        fecha = models.DateField
        descripcion = models.CharField(max_length=200)
        total_vent = models.IntegerField(max_length=200)
        id_descuento = models.ForeignKey(Descuento, on_delete=models.PROTECT)
        id_producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
        id_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
        id_categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

class Carrito (models.Model):
    id_carrito = models.IntegerField(primary_key = True, max_length=7)
    id_producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    id_venta = models.ForeignKey(Venta, on_delete=models.PROTECT)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)


class Despacho (models.Model):
        id_despacho = models.IntegerField(primary_key = True, max_length=7)
        fecha = models.DateField
        descripcion = models.CharField(max_length=200)
        direccion = models.CharField(max_length=50)
        id_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
        id_venta = models.ForeignKey(Venta, on_delete=models.PROTECT)


class Estado_despacho (models.Model):
        id_estado_despacho = models.IntegerField(primary_key = True, max_length=1)
        descripcion = models.CharField(max_length=30)
        id_despacho = models.ForeignKey(Despacho, on_delete=models.PROTECT)
        


class Historial(models.Models):
        id_historial = models.IntegerField(primary_key = True, max_length=1)
        id_despacho = models.ForeignKey(Despacho, on_delete=models.PROTECT)
        id_venta = models.ForeignKey(Venta, on_delete=models.PROTECT)


