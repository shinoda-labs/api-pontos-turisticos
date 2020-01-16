from rest_framework.viewsets import ModelViewSet
from comentario.models import Comentario
from .serializers import ComentariosSerializer


class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentariosSerializer
