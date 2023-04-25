from django.contrib import admin
from .models import Treinador, Tipo, Pokemon

# Register your models here.
admin.site.register(Treinador)
admin.site.register(Pokemon)
admin.site.register(Tipo)