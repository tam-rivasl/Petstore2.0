
from rest_framework import routers, serializers, viewsets
#models
from core.models import Usuario
##heredamos modelos principales
class Usuarioserializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields='__all__'
        exclude = ['id_usuario','nombre','apellidoPaterno','apellidoMaterno','contraseña','telefono','direccion','comuna','region']

        