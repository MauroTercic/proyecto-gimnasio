# Generated by Django 3.2.9 on 2024-01-31 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website_gym', '0002_ejercicio_rutina'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ejercicio',
            old_name='ejericio',
            new_name='ejercicio',
        ),
    ]