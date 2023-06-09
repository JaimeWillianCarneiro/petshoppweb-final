# Generated by Django 4.2 on 2023-04-18 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_animal_sexo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='sobrenome',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='animal',
            name='sexo',
            field=models.CharField(choices=[('F', 'F'), ('M', 'M')], max_length=6),
        ),
    ]
