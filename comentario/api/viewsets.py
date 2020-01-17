from rest_framework.viewsets import ModelViewSet
from comentario.models import Comentario
from .serializers import ComentariosSerializer


class ComentarioViewSet(ModelViewSet):
    serializer_class = ComentariosSerializer

    def get_queryset(self):
        return Comentario.objects.filter(aprovado=True)
