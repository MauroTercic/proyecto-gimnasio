# Generated by Django 3.2.9 on 2024-03-01 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_gym', '0004_tusejercicios_tusrutinas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tusejercicios',
            name='ejercicio',
            field=models.CharField(default='Nada', max_length=50),
        ),
        migrations.AlterField(
            model_name='tusejercicios',
            name='repeticiones',
            field=models.CharField(default='Todas', max_length=50),
        ),
        migrations.AlterField(
            model_name='tusrutinas',
            name='dias',
            field=models.CharField(default='Lunes', max_length=50),
        ),
        migrations.AlterField(
            model_name='tusrutinas',
            name='grupo_a_ejercitar',
            field=models.CharField(default='Cuerpo', max_length=50),
        ),
    ]
