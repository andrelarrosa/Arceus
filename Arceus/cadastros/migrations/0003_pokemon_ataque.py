# Generated by Django 4.1.5 on 2023-07-31 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cadastros", "0002_treinador_usuario_alter_ataque_tipo"),
    ]

    operations = [
        migrations.AddField(
            model_name="pokemon",
            name="ataque",
            field=models.ManyToManyField(to="cadastros.ataque"),
        ),
    ]
