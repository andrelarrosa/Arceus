from django import template

register = template.Library()

@register.filter(name="pertence_ao")
def pertence_ao(usuario, grupo):
    g = usuario.groups.filter(name=grupo)
    if(g.exists()):
        return True
    return False


@register.filter(name="quantidade_ataques")
def quantidade_ataques_pokemon(pokemon):
    ataques = pokemon.ataque.count()
    if(count > 4):
        return False
    
    return True