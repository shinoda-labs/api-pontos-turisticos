from rest_framework.viewsets import ModelViewSet
from comentarios.models import Comentario
from .serializers import ComentariosSerializer


class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentariosSerializer
