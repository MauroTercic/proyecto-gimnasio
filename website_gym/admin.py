from django.contrib import admin
from .models import DatosPersonales, Ejercicio, Rutina, TusEjercicios, TusRutinas, UsuarioRutinas
# Register your models here.

admin.site.register(DatosPersonales)
admin.site.register(Ejercicio)
admin.site.register(Rutina)
admin.site.register(TusEjercicios)
admin.site.register(TusRutinas)
admin.site.register(UsuarioRutinas)