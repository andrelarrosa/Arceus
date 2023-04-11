from django.urls import path

from .views import TreinadorCreate, TreinadorList, TipoCreate, TipoList

urlpatterns = [

    path("cadastrar/treinador/", TreinadorCreate.as_view(),
         name="cadastrar-treinador"),
    path("listar/treinador/", TreinadorList.as_view(), name="listar-treinador"),


    path("cadastrar/tipo/", TipoCreate.as_view(),
         name="cadastrar-tipo"),
    path("listar/tipo/", TipoList.as_view(), name="listar-tipo"),

    

]
