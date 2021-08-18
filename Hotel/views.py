from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from .models import Rol, Persona, Habitacion, RegistroHuespedes, Reserva, Servicios, Pago
from django.views.decorators.csrf import csrf_protect
# Create your views here.


def index(request):
    return HttpResponse("Funcionando")


def registrar(request):
    return HttpResponse("registrar")
