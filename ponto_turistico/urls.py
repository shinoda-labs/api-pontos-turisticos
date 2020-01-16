from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet
from atracao.api.viewsets import AtracaoViewSet
from localizacao.api.viewsets import LocalizacaoViewSet
from comentario.api.viewsets import ComentarioViewSet

routers = routers.DefaultRouter()
routers.register(r'pontosturisticos', PontoTuristicoViewSet)
routers.register(r'atracao', AtracaoViewSet)
routers.register(r'localizacoes', LocalizacaoViewSet)
routers.register(r'comentario', ComentarioViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('admin/', admin.site.urls),
]
