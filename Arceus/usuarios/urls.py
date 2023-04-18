from django.urls import path
from django.contrib.auth import auth_views

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(
            template_name = "cadastros/form.html"
            ), name="login"),
]
