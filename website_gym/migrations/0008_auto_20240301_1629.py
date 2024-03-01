# Generated by Django 3.2.9 on 2024-03-01 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_gym', '0007_remove_tusrutinas_grupo_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tusrutinas',
            name='usuario',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='tusrutinas',
            name='dias',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='tusrutinas',
            name='grupo_a_ejercitar',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]
