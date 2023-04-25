from django.shortcuts import render

from .models import Treinador, Pokemon, Tipo, Time, PokemonsTime, Ataque, AtaquesPokemon
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView


class TreinadorCreate(CreateView):
    model = Treinador
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-treinador')


class TipoCreate(CreateView):
    model = Tipo
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-tipo')


class PokemonCreate(CreateView):
    model = Pokemon
    fields = ['nome', 'tipo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pokemon')


class TimeCreate(CreateView):
    model = Time
    fields = ['nome', 'treinador']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-time')


class PokemonsTimeCreate(CreateView):
    model = PokemonsTime
    fields = ['pokemon', 'time']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pokemons-time')


class AtaqueCreate(CreateView):
    model = Ataque
    fields = ['nome', 'tipo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ataque')


class AtaquesPokemonCreate(CreateView):
    model = AtaquesPokemon
    fields = ['pokemon', 'ataque']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ataquesPokemon')

#################################################################################

class TreinadorList(ListView):
    model = Treinador
    template_name = "cadastros/list/treinador-list.html"


class TipoList(ListView):
    model = Tipo
    template_name = 'cadastros/list/treinador-list.html'


class PokemonList(ListView):
    model = Pokemon
    template_name = "cadastros/list/treinador-list.html"


class TimeList(ListView):
    model = Time
    template_name = "cadastros/list/treinador-list.html"


class PokemonsTimeList(ListView):
    model = PokemonsTime
    template_name = "cadastros/list/treinador-list.html"


class AtaqueList(ListView):
    model = Ataque
    template_name = "cadastros/list/treinador-list.html"


class AtaquesPokemonList(ListView):
    model = AtaquesPokemon
    template_name = "cadastros/list/treinador-list.html"

#################################################################################

class TreinadorUpdate(UpdateView):
    model = Treinador
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-treinador')


class TipoUpdate(UpdateView):
    model = Tipo
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-tipo')


class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = ['nome', 'tipo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pokemon')


class TimeUpdate(UpdateView):
    model = Time
    fields = ['nome', 'treinador']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pokemon')


class PokemonsTimeUpdate(UpdateView):
    model = PokemonsTime
    fields = ['pokemon', 'time']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pokemons-time')


class AtaqueUpdate(UpdateView):
    model = Ataque
    fields = ['nome', 'tipo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ataque')


class AtaquesPokemonUpdate(UpdateView):
    model = AtaquesPokemon
    fields = ['pokemon', 'ataque']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ataquesPokemon')


#################################################################################

class TreinadorDelete(DeleteView):
    model = Treinador
    template_name = ""
    success_url = reverse_lazy('listar-treinador')


class TipoDelete(DeleteView):
    model = Tipo
    template_name = ""
    success_url = reverse_lazy('listar-tipo')


class PokemonDelete(DeleteView):
    model = Pokemon
    template_name = ""
    success_url = reverse_lazy('listar-pokemon')


class TimeDelete(DeleteView):
    model = Time
    template_name = ""
    success_url = reverse_lazy('listar-time')


class PokemonsTimeDelete(DeleteView):
    model = PokemonsTime
    template_name = ""
    success_url = reverse_lazy('listar-pokemons-time')


class AtaqueDelete(DeleteView):
    model = Ataque
    template_name = ""
    success_url = reverse_lazy('listar-ataque')


class AtaquesPokemonDelete(DeleteView):
    model = AtaquesPokemon
    template_name = ""
    success_url = reverse_lazy('listar-ataquesPokemon')
