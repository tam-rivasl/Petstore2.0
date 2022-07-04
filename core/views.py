
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,'index.html')

def bandanas(request):
    return render(request,'bandanas.html')

def contacto(request):
    return render(request,'contacto.html')

def correas(request):
    return render(request,'correas.html')

def donaciones(request):
    return render(request,'donaciones.html')

def footer(request):
    return render(request,'footer.html')

def identificaciones(request):
    return render(request,'identificaciones.html')

def nav(request):
    return render(request,'nav.html')


def nosotros(request):
    return render(request,'nosotros.html')

def seguimiento(request):
    return render(request,'seguimiento.html')

def tienda(request):
    return render(request,'tienda.html')

def inicio(request):
    return render(request,'inicio.html')






