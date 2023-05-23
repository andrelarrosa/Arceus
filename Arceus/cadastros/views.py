from django.shortcuts import render

from .models import Treinador, Pokemon, Tipo, Time, PokemonsTime, Ataque, AtaquesPokemon
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView



class TreinadorCreate(CreateView):
    model = Treinador
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-treinador')
    extra_context = {'titulo': 'Inserir Treinador'}
    def form_valid(self, form):
        if(form.instance.nome == ""):
            print("Arrow")
            return form.add_error(None, "Tem que ser informado um nome para o Treinador")
        
        form.instance.usuario = self.request.user

        url = self.form_valid(form)

        return url




class TipoCreate(CreateView):
    model = Tipo
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-tipo')
    extra_context = {'titulo': 'Inserir Tipo'}
    def form_valid(self, form):
        if(form.instance.nome == ""):
            print("Arrow")
            form.add_error("nome", "Tem que ser informado um nome para o Treinador")
            return self.form_invalid(form)
        url = self.form_valid(form)

        return url


class PokemonCreate(CreateView):
    model = Pokemon
    fields = ['nome', 'tipo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pokemon')
    extra_context = {'titulo': 'Inserir Pokémon'}


class TimeCreate(CreateView):
    model = Time
    fields = ['nome', 'treinador']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-time')
    extra_context = {'titulo': 'Inserir Time'}

        


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
    extra_context = {'titulo': 'Inserir Ataque'}


class AtaquesPokemonCreate(CreateView):
    model = AtaquesPokemon
    fields = ['pokemon', 'ataque']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ataquesPokemon')

#################################################################################

class TreinadorList(ListView):
    model = Treinador
    template_name = "cadastros/list/list-treinador.html"


class TipoList(ListView):
    model = Tipo
    template_name = 'cadastros/list/list-tipo.html'


class PokemonList(ListView):
    model = Pokemon
    template_name = "cadastros/list/list-pokemon.html"


class TimeList(ListView):
    model = Time
    template_name = "cadastros/list/list.html"


class PokemonsTimeList(ListView):
    model = PokemonsTime
    template_name = "cadastros/list/list.html"


class AtaqueList(ListView):
    model = Ataque
    template_name = "cadastros/list/list-ataque.html"


class AtaquesPokemonList(ListView):
    model = AtaquesPokemon
    template_name = "cadastros/list/list.html"

#################################################################################

class TreinadorUpdate(UpdateView):
    model = Treinador
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-treinador')
    extra_context = {'titulo': 'Editar Treinador'}


class TipoUpdate(UpdateView):
    model = Tipo
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-tipo')
    extra_context = {'titulo': 'Editar Tipo'}



class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = ['nome', 'tipo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pokemon')
    extra_context = {'titulo': 'Editar Pokémon'}


class TimeUpdate(UpdateView):
    model = Time
    fields = ['nome', 'treinador']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pokemon')
    extra_context = {'titulo': 'Editar Time'}


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
    extra_context = {'titulo': 'Editar Ataque'}


class AtaquesPokemonUpdate(UpdateView):
    model = AtaquesPokemon
    fields = ['pokemon', 'ataque']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ataquesPokemon')


#################################################################################

class TreinadorDelete(DeleteView):
    model = Treinador
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy('listar-treinador')


class TipoDelete(DeleteView):
    model = Tipo
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy('listar-tipo')


class PokemonDelete(DeleteView):
    model = Pokemon
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy('listar-pokemon')


class TimeDelete(DeleteView):
    model = Time
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy('listar-time')


class PokemonsTimeDelete(DeleteView):
    model = PokemonsTime
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy('listar-pokemons-time')


class AtaqueDelete(DeleteView):
    model = Ataque
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy('listar-ataque')


class AtaquesPokemonDelete(DeleteView):
    model = AtaquesPokemon
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy('listar-ataquesPokemon')
#########################################################

class IndexView(TemplateView):
    template_name = "cadastros/sobre.html"