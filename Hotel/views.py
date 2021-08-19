from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from rest_framework import serializers
from .models import Rol, Persona, Habitacion, RegistroHuespedes, Reserva, Servicios, Pago
from django.views.decorators.csrf import csrf_exempt, csrf_protect
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

