from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

from .views import *
from django.contrib.auth import views

urlpatterns = [

    path("cadastrar/treinador/", TreinadorCreate.as_view(),
         name="cadastrar-treinador"),
    path("listar/treinador/", TreinadorList.as_view(), name="listar-treinador"),
    path("alterar/treinador/<int:pk>/", TreinadorUpdate.as_view(), name="alterar-treinador"),
    path("deletar/treinador/<int:pk>/", TreinadorDelete.as_view(), name="deletar-treinador"),


    path("cadastrar/tipo/", TipoCreate.as_view(),
         name="cadastrar-tipo"),
    path("listar/tipo/", TipoList.as_view(), name="listar-tipo"),
    path("alterar/tipo/<int:pk>", TipoUpdate.as_view(), name="alterar-tipo"),
    path("deletar/tipo/<int:pk>/", TipoDelete.as_view(), name="deletar-tipo"),

    path("cadastrar/pokemon/", PokemonCreate.as_view(),
         name="cadastrar-pokemon"),
    path("listar/pokemon/", PokemonList.as_view(), name="listar-pokemon"),
    path("alterar/pokemon/<int:pk>", PokemonUpdate.as_view(), name="alterar-pokemon"),
    path("deletar/pokemon/<int:pk>/", PokemonDelete.as_view(), name="deletar-pokemon"),


    path("cadastrar/time/", TimeCreate.as_view(), name="cadastrar-time"),
    path("listar/time/", TimeList.as_view(), name="listar-time"),
    path("alterar/time/<int:pk>", TimeUpdate.as_view(), name="alterar-time"),
    path("deletar/time/<int:pk>", TimeDelete.as_view(), name="deletar-time"),


    path("cadastrar/ataque/", AtaqueCreate.as_view(), name="cadastrar-ataque"),
    path("listar/ataque/", AtaqueList.as_view(), name="listar-ataque"),
    path("alterar/ataque/<int:pk>", AtaqueUpdate.as_view(), name="alterar-ataque"),
    path("deletar/ataque/<int:pk>", AtaqueDelete.as_view(), name="deletar-ataque"),


    path("cadastrar/pokemonsTime/", PokemonsTimeCreate.as_view(), name="cadastrar-pokemons-time"),
    path("listar/pokemonsTime/", PokemonsTimeList.as_view(), name="listar-pokemons-time"),
    path("alterar/pokemonsTime/<int:pk>", PokemonsTimeUpdate.as_view(), name="alterar-pokemons-time"),
    path("deletar/pokemonsTime/<int:pk>", PokemonsTimeDelete.as_view(), name="deletar-pokemons-time"),


    path("cadastrar/ataquesPokemon/", AtaquesPokemonCreate.as_view(), name="cadastrar-ataquesPokemon"),
    path("listar/ataquesPokemon/", AtaquesPokemonList.as_view(), name="listar-ataquesPokemon"),
    path("alterar/ataquesPokemon/<int:pk>", AtaquesPokemonUpdate.as_view(), name="alterar-ataquesPokemon"),
    path("deletar/ataquesPokemon/<int:pk>", AtaquesPokemonDelete.as_view(), name="deletar-ataquesPokemon"),


     path('alterar-minha-senha/', auth_views.PasswordChangeView.as_view(
          template_name='cadastros/login.html',
          extra_context={'titulo': 'Alterar senha atual'},
          success_url=reverse_lazy('index')
     ), name="alterar-senha"),

     path('sobre/', IndexView.as_view(), name="sobre"),
     path('', views.LoginView.as_view(
         template_name="cadastros/login.html",
         extra_context={'titulo': 'Autenticação'}
         ), name="index"),
    path('logout/', views.LoginView.as_view(
         template_name="cadastros/login.html",
         extra_context={'titulo': 'Autenticação'}
         ),name="logout")
]
