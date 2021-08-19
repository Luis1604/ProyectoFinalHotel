from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from .models import Rol, Persona, Habitacion, RegistroHuespedes, Reserva, Servicios, Pago
from django.views.decorators.csrf import csrf_protect
from .forms import FormPago, FormPersona, FormReserva
# Create your views here.


def index(request):
    return HttpResponse("Funcionando")


def registrar(request):
    return HttpResponse("registrar")

@csrf_protect
def login_view(request):
    return render(request, "login.html", {})

@csrf_protect
def inicio_view(request):
    f = FormPersona(request.POST or None)
    if request.method == 'POST':
        if f.is_valid():
            datos = f.cleaned_data
            c = Persona()
            r=Rol()
            c.Rol = Ro
            c.Nombre = datos.get("Nombre")
            c.Apellido = datos.get("Apellido")
            c.cedula = datos.get("cedula")
            c.Email = datos.get("Email")
            c.Telefono = datos.get("Telefono")
            c.Direccion = datos.get("Direccion")
            c.password = datos.get("password")
            if c.save() != True:
                print('Imprimo en pantalla y guardo data en BD')
                print(f.cleaned_data)
                return redirect(inicio_view)
    context = {
        "form":f,
    }
    return render(request, "inicio.html", {})

def reserva_view(request):
    return render(request, "reserva.html", {})

def servicio_view(request):
    return render(request, "servicios.html", {})
