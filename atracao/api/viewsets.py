from rest_framework.viewsets import ModelViewSet
from atracao.models import Atracao
from atracao.api.serializers import AtracoesSerializer


class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracoesSerializer
