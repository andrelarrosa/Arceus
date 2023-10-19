from django import template

register = template.Library()

@register.filter(name="pertence_ao")
def pertence_ao(usuario, grupo):
    g = usuario.groups.filter(name=grupo)
    if(g.exists()):
        return True
    return False


@register.filter(name="quantidade_ataques")
def quantidade_ataques_pokemon(pokemon, id):
    quantidade = pokemon.ataque.filter(pokemon__id=id).count()
    return quantidade


@register.filter(name="tipo_ataque")
def tipo_ataque_count(ataque):
    return ataque.tipo