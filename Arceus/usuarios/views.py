from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import UsuarioForm 

class UsuarioCreate(CreateView):
    template_name = "cadastros/form.html"
    # model = User
    # fields = ['username', 'email', 'password']
    form_class = UsuarioForm
    success_url = '../login'

