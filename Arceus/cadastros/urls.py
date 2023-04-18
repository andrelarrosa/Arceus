from django.urls import path

from .views import TreinadorCreate, TreinadorUpdate, TreinadorList, TipoCreate, TipoList, PokemonCreate, PokemonList

urlpatterns = [

    path("cadastrar/treinador/", TreinadorCreate.as_view(),
         name="cadastrar-treinador"),
    path("editar/treinador/<int:pk>/", TreinadorUpdate.as_view(), name="editar-treinador"),
    path("listar/treinador/", TreinadorList.as_view(), name="listar-treinador"),


    path("cadastrar/tipo/", TipoCreate.as_view(),
         name="cadastrar-tipo"),
    path("listar/tipo/", TipoList.as_view(), name="listar-tipo"),

    path("cadastrar/pokemon/", PokemonCreate.as_view(),
         name="cadastrar-pokemon"),
    path("listar/pokemon/", PokemonList.as_view(), name="listar-pokemon")
    

]
