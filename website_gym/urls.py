from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('ver_datos/', views.ver_datos, name="ver_datos"),
    path('editar_datos/', views.editar_datos, name="editar_datos"),
    path('rutinas/', views.rutinas, name="rutinas"),
    path('rutina/<int:pk>', views.rutina, name="rutina"),
    path('sobre_nosotros/', views.sobre_nosotros, name="sobre_nosotros"),

]
