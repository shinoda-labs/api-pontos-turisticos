from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracoesViewSet

routers = routers.DefaultRouter()
routers.register(r'pontoturistico', PontoTuristicoViewSet)
routers.register(r'atracoes', AtracoesViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('admin/', admin.site.urls),
]
