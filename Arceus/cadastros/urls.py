from django.urls import path

from .views import TreinadorCreate, TreinadorUpdate, TreinadorList, TipoCreate, TipoList, PokemonCreate, PokemonList, TimeCreate, TimeList, PokemonsTimeCreate, AtaqueCreate, AtaquesPokemonCreate, AtaqueList, PokemonsTimeList, TreinadorDelete

urlpatterns = [

    path("cadastrar/treinador/", TreinadorCreate.as_view(),
         name="cadastrar-treinador"),
    path("listar/treinador/", TreinadorList.as_view(), name="listar-treinador"),
    path("alterar/treinador/<int:pk>/", TreinadorUpdate.as_view(), name="alterar-treinador"),
    path("deletar/treinador/<int:pk>/", TreinadorDelete.as_view(), name="deletar-treinador"),


    path("cadastrar/tipo/", TipoCreate.as_view(),
         name="cadastrar-tipo"),
    path("listar/tipo/", TipoList.as_view(), name="listar-tipo"),

    path("cadastrar/pokemon/", PokemonCreate.as_view(),
         name="cadastrar-pokemon"),
    path("listar/pokemon/", PokemonList.as_view(), name="listar-pokemon"),

    path("cadastrar/time/", TimeCreate.as_view(),
         name="cadastrar-time"),
    path("listar/time/", TimeList.as_view(), name="listar-time"),

    path("cadastrar/ataque/", AtaqueCreate.as_view(),
         name="cadastrar-ataque"),
    path("listar/ataque/", AtaqueList.as_view(), name="listar-ataque"),
    path("cadastrar/pokemonsTime/", PokemonsTimeCreate.as_view(),
         name="cadastrar-pokemons-time"),
    path("listar/PokemonsTime/", PokemonsTimeList.as_view(), name="listar-pokemons-time"),


    path("cadastrar/ataquesPokemon/", AtaquesPokemonCreate.as_view(),
         name="cadastrar-ataquesPokemon"),
    path("listar/ataque/", TimeList.as_view(), name="listar-ataquesPokemon"),


]
