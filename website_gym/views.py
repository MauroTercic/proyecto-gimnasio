from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, EditarDatos, EditarRutinas, EditarEjercicios
from .models import DatosPersonales, Rutina, Ejercicio, TusRutinas, TusEjercicios, UsuarioRutinas
import datetime as dt



def home(request):
    # El form para logear en home page
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # Si el usuari es real loggearlo
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Ingresaste correctamente.")
            return redirect("home")
        else:
            messages.success(request, "Hubo un error al ingresar, intente de nuevo.")
            return redirect("home")
    else:
        return render(request, "home.html", {})



def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Cerraste sesión.")
        return redirect("home")



def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Te registraste correctamente")

            # Crea su entry en la base de datos de datos personales
            modelo_usuario = DatosPersonales(usuario=username)
            modelo_usuario.save()

            # Crea su entry en la base de datos de tus rutinas
            modelo_usuario_rutinas = UsuarioRutinas(usuario=username)
            modelo_usuario_rutinas.save()

            # Crea tu entry en la base de datos de tus rutinas
            dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
            for i in dias:
                modelo_rutinas = TusRutinas(dias=i, grupo_id=UsuarioRutinas.objects.get(usuario=user)) 
                modelo_rutinas.save()

            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})



def ver_datos(request):
    # Solo si el usuario esta loggeado
    if request.user.is_authenticated:
        datos = DatosPersonales.objects.filter(usuario=request.user)
        return render(request, "ver_datos.html", {"datos":datos})
    


def editar_datos(request):
    # Solo si el usuario esta loggeado
    if request.user.is_authenticated:
        datos = DatosPersonales.objects.get(usuario=request.user)
        form = EditarDatos(request.POST or None, instance=datos)
        if form.is_valid():
            form.save()
            messages.success(request, "Actualizaste tus datos correctamente.")
            return redirect("ver_datos")
        return render(request, "editar_datos.html", {"form":form})
    else:
        return redirect("home")
    


def rutinas_todos(request):
    # Solo si el usuario esta loggeado
    if request.user.is_authenticated:
        # Tomar el dia de la fecha para mostrar primero esa rutina
        date = dt.datetime.today().weekday()
        # Como solo hay rutinas para los dias habiles chequear que sea entre 1 (lunes) y 5 (viernes)
        if date < 5:
            semana = {0:"Lunes", 1:"Martes", 2:"Miercoles", 3:"Jueves", 4:"Viernes",}
            dia = semana[date]
            datos_rutinas = Rutina.objects.get(dias=dia)
            datos_ejercicios = Ejercicio.objects.filter(grupo_id=datos_rutinas.id)

            return render(request, "rutinas.html", {"datos_rutinas":datos_rutinas, "datos_ejercicios":datos_ejercicios})
        
        # Si es fin de semana mostrar la rutina del lunes
        datos_rutinas_lunes = Rutina.objects.get(dias="Lunes")
        datos_ejercicios_lunes = Ejercicio.objects.filter(grupo_id=datos_rutinas_lunes.id)
        return render(request, "rutinas.html", {"datos_rutinas":datos_rutinas_lunes, "datos_ejercicios":datos_ejercicios_lunes})
    

def rutina_todos(request, pk):
    datos_rutinas = Rutina.objects.get(id=pk)
    datos_ejercicios = Ejercicio.objects.filter(grupo_id=datos_rutinas.id)
    return render(request, "rutina.html", {"datos_rutinas":datos_rutinas, "datos_ejercicios":datos_ejercicios})


def tus_rutinas(request):
    # Solo si el usuario esta loggeado
    if request.user.is_authenticated:
        # Tomar el dia de la fecha para mostrar primero esa rutina
        date = dt.datetime.today().weekday()
        # Como solo hay rutinas para los dias habiles chequear que sea entre 1 (lunes) y 5 (viernes)
        if date < 5:
            semana = {0:"Lunes", 1:"Martes", 2:"Miercoles", 3:"Jueves", 4:"Viernes",}
            dia = semana[date]
            datos_rutinas = TusRutinas.objects.get(dias=dia)
            datos_ejercicios = TusEjercicios.objects.filter(grupo_id=datos_rutinas.id)
            return render(request, "tus_rutinas.html", {"datos_rutinas":datos_rutinas, "datos_ejercicios":datos_ejercicios})
        
def editar_tus_rutinas(request):
    if request.user.is_authenticated:
        datos = TusRutinas.objects.get(usuario=request.user)
        form = EditarRutinas(request.POST or None, instance=datos)
        if form.is_valid():
            form.save()
            messages.success(request, "Actualizaste tus datos correctamente.")
            return redirect("ver_datos")
        return render(request, "editar_tus_rutinas.html", {"form":form})
    else:
        return redirect("home")



def tus_rutinas_detalle(request,pk):
    datos_rutinas = TusRutinas.objects.get(id=pk)
    datos_ejercicios = TusEjercicios.objects.filter(grupo_id=datos_rutinas.id)
    return render(request, "tus_rutinas_detalles.html", {"datos_rutinas":datos_rutinas, "datos_ejercicios":datos_ejercicios})

def editar_tus_rutinas_detalles(request):
    return render(request, "editar_tus_rutinas_detalles.html", {})


def sobre_nosotros(request):
    return render(request, "sobre_nosotros.html", {})