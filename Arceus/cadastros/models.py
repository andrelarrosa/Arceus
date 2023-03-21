from django.db import models

# Create your models here.
class Treinador(models.Model):
    nome = models.CharField(max_length=100);

    def __str__(self):
        return f"{self.nome}";


class Tipo(models.Model):
    nome = models.CharField(max_length=50);

    def __str__(self):
        return f"{self.nome}"


class Pokemon(models.Model):
    nome = models.CharField(max_length=100)


class TiposPokemon(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT);
    pokemon = models.ForeignKey(Pokemon, on_delete=models.PROTECT);



