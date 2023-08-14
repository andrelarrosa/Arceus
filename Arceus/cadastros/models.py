from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Treinador(models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nome}"


class Tipo(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome}"


class Time(models.Model):
    nome = models.CharField(max_length=200)
    treinador = models.ForeignKey(Treinador, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.nome}"

class Ataque(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome}"


class Pokemon(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.ManyToManyField(Tipo)
    ataque = models.ManyToManyField(Ataque)

    def __str__(self):
        return f"{self.nome}"  


class PokemonsTime(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.PROTECT)
    time = models.ForeignKey(Time, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.time}"
    

class AtaquesPokemon(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.PROTECT)
    ataque = models.ForeignKey(Ataque, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome}"
