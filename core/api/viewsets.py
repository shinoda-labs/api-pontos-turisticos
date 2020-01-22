from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(status=True)

    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        return Response({'data': f'ID: {pk} denunciada.'})

    @action(methods=['post'], detail=False)
    def teste(self, request):
        pass
