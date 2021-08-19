from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from rest_framework import serializers
from .models import Rol, Persona, Habitacion, RegistroHuespedes, Reserva, Servicios, Pago
from django.views.decorators.csrf import csrf_exempt
from .forms import FormPago, FormPersona, FormReserva
from .serializers import personaSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
# Create your views here.


def index(request):
    return HttpResponse("Funcionando")


@csrf_exempt
def registrar_list(request):
    if request.method == 'GET':
        persona = Persona.objects.all()
        serializer = personaSerializer(persona, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = personaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def registrar_detail(request, pk):
    try:
        persona = Persona.objects.get(pk=pk)
    except Persona.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = personaSerializer(persona)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = personaSerializer(persona, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

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
