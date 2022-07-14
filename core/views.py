
from itertools import product
from re import template
from django.shortcuts import redirect, render

from core.forms import *
from .models import Carrito, Estado_despacho, Producto  



def index(request):
    template_name = "index.html"
    return render(request, template_name)

def bandanas(request):
    template_name = "bandanas.html"
    return render(request, template_name)

def contacto(request):
    template_name = "contacto.html"
    return render(request, template_name)

def correas(request):
    template_name = "correas.html"
    return render(request,template_name)

def donaciones(request):
    template_name = "donaciones.html"
    return render(request, template_name)

def footer(request):
    template_name = "footer.html"
    return render(request, template_name)

def identificaciones(request):
    template_name = "identificaciones.html"
    return render(request, template_name)

def nav(request):
    template_name = "nav.html"
    return render(request, template_name)

def nosotros(request):
    template_name = "nosotros.html"
    return render(request, template_name)

def seguimiento(request):
    template_name = "seguimiento.html"

    estado_despacho = Estado_despacho.objects.all
    data = {
        'estado_despacho': estado_despacho
    }
    return render(request, template_name, data)

def tienda(request):
    template_name = "tienda.html"
    producto = Producto.objects.all

    data = {
        'producto': producto
    }
    return render(request,template_name, data)

def inicio(request):
    template_name = "inicio.html"
    return render(request, template_name)

def login(request):
    template_name = "login.html"
    return render(request, template_name)
   

def ofertas(request):
    template_name = "oferta.html"
    return render(request, template_name)


def carrito(request):
    carrito = Carrito.objects.all
    
    data = {
        'carrito': carrito
    }
    return render(request,'carrito.html', data)

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")

def registro(request):
    template_name = "registro.html"
    return render(request, template_name)





