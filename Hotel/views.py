from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Rol, Persona, Habitacion, RegistroHuespedes, Reserva, Servicios, Pago
from django.views.decorators.csrf import csrf_protect
# Create your views here.
