from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import DatosPersonales


# Create your views here.
def home(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

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

            # Crea su entry en la base de datos
            modelo_usuario = DatosPersonales(usuario=username)
            modelo_usuario.save()

            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})


def ver_datos(request):
    if request.user.is_authenticated:
        datos = DatosPersonales.objects.filter(usuario=request.user)
        return render(request, "ver_datos.html", {"datos":datos})