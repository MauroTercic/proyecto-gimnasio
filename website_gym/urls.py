from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('ver_datos/', views.ver_datos, name="ver_datos"),
    path('editar_datos/', views.editar_datos, name="editar_datos"),
    path('rutinas_todos/', views.rutinas_todos, name="rutinas_todos"),
    path('rutina_todos/<int:pk>', views.rutina_todos, name="rutina_todos"),
    path('tus_rutinas/', views.tus_rutinas, name="tus_rutinas"),
    path('editar_tus_rutinas/', views.editar_tus_rutinas, name="editar_tus_rutinas"),
    path('tus_rutina/<int:pk>', views.tus_rutinas_detalle, name="tus_rutinas_detalle"),
    path('editar_tus_rutinas_detalles/', views.editar_tus_rutinas_detalles, name="editar_tus_rutinas_detalles"),
    path('sobre_nosotros/', views.sobre_nosotros, name="sobre_nosotros"),
]
