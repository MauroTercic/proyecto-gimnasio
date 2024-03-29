from typing import Any
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DatosPersonales(models.Model):
    usuario = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50, null=True)
    apellido = models.CharField(max_length=50, null=True)
    peso = models.FloatField(default=0)
    masa = models.FloatField(default=0)
    grasa = models.FloatField(default=0)
    cintura = models.FloatField(default=0)
    brazo = models.FloatField(default=0)
    pierna = models.FloatField(default=0)
    pecho = models.FloatField(default=0)
    pecho_respirado = models.FloatField(default=0)
    brazo_trabado = models.FloatField(default=0)
    altura = models.FloatField(default=0)
    edad = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.usuario




class Rutina(models.Model):
    dias = models.CharField(max_length=50)
    grupo_a_ejercitar = models.CharField(max_length=50)


class Ejercicio(models.Model):
    ejercicio = models.CharField(max_length=50)
    repeticiones = models.CharField(max_length=50)
    grupo_id = models.ForeignKey(Rutina, on_delete=models.CASCADE)


class UsuarioRutinas(models.Model):
    usuario = models.CharField(max_length=50)

class TusRutinas(models.Model):
    dias = models.CharField(max_length=50)
    grupo_a_ejercitar = models.CharField(max_length=50, default=None, null=True)
    grupo_id = models.ForeignKey(UsuarioRutinas, on_delete=models.CASCADE)


class TusEjercicios(models.Model):
    ejercicio = models.CharField(max_length=50, default=None)
    repeticiones = models.CharField(max_length=50, default=None)
    grupo_id = models.ForeignKey(TusRutinas, on_delete=models.CASCADE)