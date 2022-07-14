from dataclasses import field
from pyexpat import model
from statistics import mode
from django import forms
from django.forms import ModelForm
from .models import *

class ProductoForm(forms.ModelForm):

    class Producto:
        model = Producto
        field =['id_producto','Nombre', 'stock', 'precio', 'id_categoria']

class UsuarioForm(forms.ModelForm):
    class Usuario:
        model = Usuario
        field =['id_producto','Nombre', 'apellidoPaterno', 'apellidoMaterno', 'email', 'contraseña', 'telefono', 'direccion', 'comuna', 'region']


class TipoUserForm(forms.ModelForm):
    class TipoUser:
        model = TipoUser
        field['id_tipoUser', 'tipoUser', 'id_usuario']


class Descuento(forms.ModelForm):
    class categoria:
        model = Categoria
        field = ['id_categoria', 'descripcion']

class Descuento(forms.ModelForm):
    class Descuento:
        model = Descuento
        field = ['id_descuento', 'promocion', 'subscripcion']

class Venta(forms.ModelForm):
    class Venta:
        model = Venta
        field = ['id_venta', 'fecha', 'descripcion', 'total_vent', 'id_descuento', 'id_producto', 'id_usuario', 'id_categoria']

class Carrito(forms.ModelForm):
    class Carrito:
        model = Carrito
        field = ['id_carrito',  'id_producto', 'id_venta', 'id_usuario']

class Despacho(forms.ModelForm):
    class Despacho:
        model = Despacho
        field = ['id_despacho', 'fecha', 'descripcion', 'direccion', 'id_usuario', 'id_venta']

class Estado_despacho(forms.ModelForm):
    class Estado_despacho:
        model = Estado_despacho
        field = ['id_estado_despacho', 'descripcion', 'id_despacho']
