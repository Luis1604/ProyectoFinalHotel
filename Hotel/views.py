from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from rest_framework import serializers
from .models import Rol, Persona, Habitacion, RegistroHuespedes, Reserva, Servicios, Pago
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .forms import FormPago, FormPersona, FormReserva
from .serializers import personaSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


def index(request):
    return HttpResponse("Funcionando")


@api_view(['GET', 'POST'])
def registrar_list(request):
    if request.method == 'GET':
        persona = Persona.objects.all()
        serializer = personaSerializer(persona, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = personaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def registrar_detail(request, pk):
    try:
        persona = Persona.objects.get(pk=pk)
    except Persona.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = personaSerializer(persona)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = personaSerializer(persona, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        persona.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
            c.Rol= Rol(2)
            c.Nombre = datos.get("Nombre")
            c.Apellido = datos.get("Apellido")
            c.cedula = datos.get("cedula")
            c.Email = datos.get("Email")
            c.Telefono = datos.get("Telefono")
            c.Direccion = datos.get("Direccion")
            c.password = datos.get("password")
            if c.save() != True:
                return redirect(inicio_view)
    context = {
        'form': f,
    }
    return render(request, "inicio.html", context)


def reserva_view(request):
    return render(request, "reserva.html", {})


def servicio_view(request):
    return render(request, "servicios.html", {})
