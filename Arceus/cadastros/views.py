from django.shortcuts import render

from .models import Treinador, Pokemon, Tipo, TiposPokemon
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView


class TreinadorCreate(CreateView):
    model = Treinador
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-treinador')


class TreinadorList(ListView):
    model = Treinador
    template_name = "cadastros/list/treinador-list.html"

class TipoCreate(CreateView):
    model = Tipo
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-tipo')

class TipoList(ListView):
    model = Tipo
    template_name = 'cadastros/list/treinador-list.html'
