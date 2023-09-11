from typing import Any, Optional
from django.db import models
from django.shortcuts import render

from .models import Treinador, Pokemon, Tipo, Time, PokemonsTime, Ataque, AtaquesPokemon
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from dal import autocomplete
from .forms import PokemonForm


class TreinadorCreate(CreateView):
    model = Treinador
    fields = ['nome', 'usuario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-treinador')
    extra_context = {'titulo': 'Inserir Treinador'}
    def form_valid(self, form):
        form.instance.usuario = self.request.user

        url = super().form_valid(form)
        
        return url


class TipoCreate(GroupRequiredMixin, CreateView):
    model = Tipo
    fields = ['nome']
    group_required = ['Administrador']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-tipo')
    extra_context = {'titulo': 'Inserir Tipo'}

    def form_valid(self, form):
        if(form.instance.nome == ""):
            form.add_error("nome", "Tem que ser informado um nome para o Treinador")
            return self.form_invalid(form)
        url = super().form_valid(form)

        return url


class PokemonCreate(GroupRequiredMixin, CreateView):
    form_class = PokemonForm
    group_required = ['Administrador']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pokemon')
    extra_context = {'titulo': 'Inserir Pokémon'}


class TimeCreate(LoginRequiredMixin, CreateView):
    model = Time
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-time')
    extra_context = {'titulo': 'Inserir Time'}

    def form_valid(self, form):
        form.instance.treinador = Treinador.objects.get(usuario=self.request.user)

        url = super().form_valid(form)

        return url


class PokemonsTimeCreate(CreateView):
    model = PokemonsTime
    fields = ['pokemon', 'time']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pokemons-time')


class AtaqueCreate(GroupRequiredMixin, CreateView):
    model = Ataque
    group_required = ['Administrador']
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

class TreinadorList(LoginRequiredMixin, ListView):
    model = Treinador
    template_name = "cadastros/list/list-treinador.html"
    def get_queryset(self):
        self.object_list = Treinador.objects.filter(usuario=self.request.user)
        return self.object_list


class TipoList(LoginRequiredMixin, ListView):
    model = Tipo
    template_name = 'cadastros/list/list-tipo.html'


class PokemonList(LoginRequiredMixin, ListView):
    model = Pokemon
    template_name = "cadastros/list/list-pokemon.html"


class TimeList(LoginRequiredMixin, ListView):
    model = Time
    template_name = "cadastros/list/list-time.html"

    def get_queryset(self):
        self.object_list = Time.objects.filter(treinador__usuario=self.request.user)
        return self.object_list


class PokemonsTimeList(LoginRequiredMixin, ListView):
    model = PokemonsTime
    template_name = "cadastros/list/list.html"
    def get_queryset(self):
        self.object_list = PokemonsTime.filter(time__treinador__usuario=self.request.user)
        return self.object_list


class AtaqueList(LoginRequiredMixin, ListView):
    model = Ataque
    template_name = "cadastros/list/list-ataque.html"


class AtaquesPokemonList(LoginRequiredMixin, ListView):
    model = AtaquesPokemon
    template_name = "cadastros/list/list.html"

#################################################################################

class TreinadorUpdate(UpdateView):
    model = Treinador
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-treinador')
    extra_context = {'titulo': 'Editar Treinador'}


class TipoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Tipo
    fields = ['nome']
    group_required = ['Administrador']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-tipo')
    extra_context = {'titulo': 'Editar Tipo'}

    def get_object(self):
        self.object = Tipo.objects.get(pk=self.kwargs["pk"])
        return self.object



class PokemonUpdate(UpdateView):
    form_class = PokemonForm
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pokemon')
    extra_context = {'titulo': 'Editar Pokémon'}
    def get_object(self):
        self.object = Pokemon.objects.get(pk=self.kwargs["pk"])
        return self.object


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


class AtaqueUpdate(GroupRequiredMixin, UpdateView):
    model = Ataque
    fields = ['nome', 'tipo']
    group_required = ['Administrador']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ataque')
    extra_context = {'titulo': 'Editar Ataque'}


class AtaquesPokemonUpdate(UpdateView):
    model = AtaquesPokemon
    fields = ['pokemon', 'ataque']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ataquesPokemon')


#################################################################################

class TreinadorDelete(GroupRequiredMixin, DeleteView):
    model = Treinador
    group_required = ['Administrador']
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy('listar-treinador')


class TipoDelete(GroupRequiredMixin, DeleteView):
    model = Tipo
    group_required = ['Administrador']
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy('listar-tipo')


class PokemonDelete(GroupRequiredMixin, DeleteView):
    model = Pokemon
    group_required = ['Administrador']
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


class AtaqueDelete(GroupRequiredMixin, DeleteView):
    model = Ataque
    group_required = ['Administrador']
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy('listar-ataque')


class AtaquesPokemonDelete(DeleteView):
    model = AtaquesPokemon
    template_name = "cadastros/delete.html"
    success_url = reverse_lazy('listar-ataquesPokemon')
#########################################################


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "cadastros/homepage.html"

    def get_context_data(self, *args, **kwargs):
    
        dados = super().get_context_data(*args, **kwargs)
        if (self.request.user.is_authenticated):
            dados["qtde_times"] = Time.objects.filter(treinador__usuario = self.request.user).count()
        
        return dados


class SobreView(TemplateView):
    template_name = "cadastros/sobre.html"


class PokemonTipoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Tipo.objects.none()
        
        qs = Tipo.objects.all()

        if self.q:
            qs = qs.filter(nome__icontains=self.q)

        return qs


class PokemonAtaqueAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Ataque.objects.none()
        
        qs = Ataque.objects.all()

        if self.q:
            qs = qs.filter(nome__icontains=self.q)

        return qs
