from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("logout/", auth_views.LoginView.as_view(
        template_name='cadastros/login.html',
        extra_context={'titulo': 'logar com outro usuário'}), name="logout"),
    path("login/", auth_views.LoginView.as_view(
        template_name='cadastros/login.html',
        extra_context={'titulo': 'Autenticação'}), name="login"),
]
