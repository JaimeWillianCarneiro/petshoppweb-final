# Generated by Django 4.2 on 2023-04-18 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_cliente_sobrenome_alter_animal_sexo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='nomeUsuario',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
