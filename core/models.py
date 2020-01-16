from django.db import models
from atracao.models import Atracao
from comentario.models import Comentario
from avaliacao.models import Avaliacao
from localizacao.models import Localizacao


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(default=None)
    status = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(Localizacao, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
