# Generated by Django 3.2.9 on 2024-03-01 19:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website_gym', '0005_auto_20240301_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='tusrutinas',
            name='grupo_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='website_gym.datospersonales'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tusejercicios',
            name='ejercicio',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='tusejercicios',
            name='repeticiones',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='tusrutinas',
            name='dias',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='tusrutinas',
            name='grupo_a_ejercitar',
            field=models.CharField(default=None, max_length=50),
        ),
    ]