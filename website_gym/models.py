from typing import Any
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DatosPersonales(models.Model):
    #usuario = models.ForeignKey(User, on_delete=models.CASCADE)
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
