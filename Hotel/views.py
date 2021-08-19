from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from rest_framework import serializers
from .models import Rol, Persona, Habitacion, RegistroHuespedes, Reserva, Servicios, Pago
from django.views.decorators.csrf import csrf_exempt
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
        data = JSONParser().parse(request)
        serializer = personaSerializer(persona, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        persona.delete()
        return HttpResponse(status=204)


def login_view(request):
    return render(request, "login.html", {})


def create_view(request):
    return render(request, "Create.html", {})


def inicio_view(request):
    return render(request, "inicio.html", {})


def reserva_view(request):
    return render(request, "reserva.html", {})
