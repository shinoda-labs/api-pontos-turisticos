from rest_framework.serializers import ModelSerializer
from comentario.models import Comentario


class ComentariosSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('id', 'usuario', 'comentario', 'data', 'aprovado')
