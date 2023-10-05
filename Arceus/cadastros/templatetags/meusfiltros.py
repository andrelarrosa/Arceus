from django import template

register = template.Library()

@register.filter(name="pertence_ao")
def pertence_ao(usuario, grupo):
    g = usuario.groups.filter(name=grupo)
    if(g.exists()):
        return True
    return False