# Generated by Django 4.1.7 on 2023-03-13 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_cliente_telefone'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='fazpedido',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='recebepedido',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.IntegerField(),
        ),
    ]