from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracaoViewSet
from localizacao.api.viewsets import LocalizacaoViewSet
from comentarios.api.viewsets import ComentarioViewSet

routers = routers.DefaultRouter()
routers.register(r'pontosturisticos', PontoTuristicoViewSet)
routers.register(r'atracoes', AtracaoViewSet)
routers.register(r'localizacoes', LocalizacaoViewSet)
routers.register(r'comentarios', ComentarioViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('admin/', admin.site.urls),
]
