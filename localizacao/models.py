from django.db import models


class LocalizacaoTipo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Localizacao(models.Model):
    rua = models.CharField(max_length=150)
    tipo = models.ForeignKey(LocalizacaoTipo, on_delete=models.CASCADE)
    numero = models.IntegerField(null=True, blank=True)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    cep = models.BigIntegerField()
    pais = models.CharField(max_length=50)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.rua





