from dal import autocomplete
from django import forms
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['nome', 'tipo', 'ataque']
        widgets = {
            'tipo': autocomplete.ModelSelect2Multiple(
                url='buscar-tipo',
                attrs={
                    'data-placeholder': 'Autocomplete ...',
                },
            ),
                
            'ataque': autocomplete.ModelSelect2Multiple(attrs={
                'data-placeholder': 'Autocomplete ...',
            },  url='buscar-ataque'),
        }
