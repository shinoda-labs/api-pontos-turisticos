from rest_framework.serializers import ModelSerializer

from localizacao.models import Localizacao


class LocalizacaoSerializer(ModelSerializer):
    class Meta:
        model = Localizacao
        fields = ('id', 'rua', 'numero', 'bairro', 'cidade', 'uf', 'cep', 'pais', 'latitude', 'longitude')
