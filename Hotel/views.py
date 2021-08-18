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

def login_view(request):
    return render(request, "login.html", {})

def create_view(request):
    return render(request, "Create.html", {})

def inicio_view(request):
    return render(request, "inicio.html", {})

def reserva_view(request):
    return render(request, "reserva.html", {})