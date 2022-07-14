from pickle import GET
from webbrowser import get
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.models import *
from .serializers import *
from django.http import Http404
# Create your views here.
##filtramos los parametros del usuario
@api_view(['GET']) 
def apiUsuario(self, request, format=None, *args, **kwargs):
    usuario = Usuario.objects.all()
    serializers = Usuarioserializers(Usuario, many=True)

    print("2 - serializers:",serializers)
    return Response(serializers.data)


@api_view(['GET'])
def getObjet(self, pk):
    try:
        return Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        raise Http404

@api_view(['GET'])
def getUser(self, request, pk, format=None):
    usuario = self.getObjet(pk)
    serializers = Usuarioserializers(usuario)
    return Response(serializers.Meta)