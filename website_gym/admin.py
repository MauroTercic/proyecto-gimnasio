from django.contrib import admin
from .models import DatosPersonales, Ejercicio, Rutina
# Register your models here.

admin.site.register(DatosPersonales)
admin.site.register(Ejercicio)
admin.site.register(Rutina)