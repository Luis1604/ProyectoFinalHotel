from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .forms import FormPago, FormPersona, FormReserva, FormLogin
from .serializers import personaSerializer
from django.http import JsonResponse, Http404
from rest_framework import serializers, status, mixins, generics, viewsets, permissions
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, APIView, action
from rest_framework.response import Response
from rest_framework import status
from .models import Rol, Persona, Habitacion, RegistroHuespedes, Reserva, Servicios, Pago
from django.contrib import messages
from .serializers import personaSerializer, habitacionSerializer, reservaSerializer, registroHuespedesSerializer, serviciosSerializer
# Create your views here.
def index(request):
    return HttpResponse("Funcionando")


class personaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = personaSerializer


class habitacionViewSet(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all()
    serializer_class = habitacionSerializer


class reservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = reservaSerializer



class registroHuespedesViewSet(viewsets.ModelViewSet):
    queryset = RegistroHuespedes.objects.all()
    serializer_class = registroHuespedesSerializer


class serviciosViewSet(viewsets.ModelViewSet):
    queryset = Servicios.objects.all()
    serializer_class = serviciosSerializer


@csrf_protect
def login_view(request):
    flogin = FormLogin(request.POST or None)
    if request.method == 'POST':
        if flogin.is_valid():
            datos = flogin.cleaned_data
            email = datos.get("Email")
            passw = datos.get("password")
            numEncontrados = Persona.objects.filter(Email = email, password=passw).count()
            print(email)
            print(numEncontrados)
            if numEncontrados > 0:
                logiado=True
                print("Inicio perfecto")
                messages.success(request, 'Bienvenido')
                return redirect(login_view)
            else:
                print("Fallo")
                messages.warning(request, 'Credenciales Incorrectas')
                return redirect(login_view)
    context = {
        'form': flogin,
    }
    return render(request, "login.html", context)

def inicio_view(request):
        return render(request, "inicio.html", {})   

@csrf_protect
def registro_view(request):
    f = FormPersona(request.POST or None)
    if request.method == 'POST':
        if f.is_valid():
            datos = f.cleaned_data
            c = Persona()
            c.Rol= Rol(2)
            c.Nombre = datos.get("Nombre")
            c.Apellido = datos.get("Apellido")
            c.cedula = datos.get("cedula")
            c.Email = datos.get("Email")
            c.Telefono = datos.get("Telefono")
            c.Direccion = datos.get("Direccion")
            c.password = datos.get("password")
            if c.save() != True:
                messages.warning(request, 'Registrado Correctamente')
                return redirect(registro_view)
    context = {
        'form': f,
    }
    return render(request, "registro.html", context)

@csrf_protect
def reserva_view(request):
    fr = FormReserva(request.POST or None)
    if request.method == 'POST':
        if  fr.is_valid():
            datos = fr.cleaned_data
            nreserva="0001"+"983"
            c = Reserva()
            c.numHabitacion = datos.get("numHabitacion")
            c.Persona = datos.get("Persona")
            c.Fecha_Ingreso = datos.get("Fecha_Ingreso")
            c.Fecha_Caducidad = datos.get("Fecha_Caducidad")
            c.numReserva = nreserva
            if c.save() != True:
                messages.warning(request, 'Reservada correctamente')
                return redirect(reserva_view)     
    context = {
        "form": fr,
    }
    return render(request, "reserva.html", context)

@csrf_protect
def servicio_view(request):
    fs = FormPago(request.POST or None)
    if request.method == 'POST':
        if  fs.is_valid():
            datos = fs.cleaned_data
            c = Pago()
            c.Servicios = datos.get("Servicios")
            c.Habitacion = datos.get("Habitacion")
            c.Nombre = datos.get("Habitacion").Reserva.Persona.Nombre
            c.Apellido = datos.get("Habitacion").Reserva.Persona.Apellido
            c.Email =  datos.get("Habitacion").Reserva.Persona.Email
            c.Detalle = ""
            c.Direccion = datos.get("Habitacion").Reserva.Persona.Direccion
            c.Total= datos.get("Habitacion").Reserva.numHabitacion.Precio + datos.get("Servicios").Precio
            c.Estado = 'Pendiente'
            if c.save() != True:
                messages.warning(request, 'Registrado Correctamente')
                return redirect(inicio_view)
    context = {
        "form": fs,
    }
    return render(request, "servicios.html", context)

