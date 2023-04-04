from django.urls import path

from .views import TreinadorCreate, TreinadorList

urlpatterns = [

    path("cadastrar/treinador/", TreinadorCreate.as_view(), name="cadastrar-treinador"),
    path("listar/treinador/", TreinadorList.as_view(), name="listar-treinador"),

]
