from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse, Http404
from rest_framework import serializers, status, mixins, generics, viewsets, permissions
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, APIView, action
from rest_framework.response import Response
from .models import Rol, Persona, Habitacion, RegistroHuespedes, Reserva, Servicios, Pago
from .forms import FormPago, FormPersona, FormReserva
from .serializers import personaSerializer
# Create your views here.


def index(request):
    return HttpResponse("Funcionando")


class registrarViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Persona.objects.all()
    serializer_class = personaSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Persona.objects.all()
    serializer_class = personaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        persona = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


'''  mixins
class registrarList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset = Persona.objects.all()
    serializer_class = personaSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class registrarDetail(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      generics.GenericAPIView):
    queryset = Persona.objects.all()
    serializer_class = personaSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
'''

''' Rewriting our API using class-based views
class registrarList(APIView):

    def get(self, request, format=None):
        persona = Persona.objects.all()
        serializer = personaSerializer(persona, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = personaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class registrarDetail(APIView):

    def get_object(self, pk):
        try:
            return Persona.objects.get(pk=pk)
        except Persona.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        persona = self.get_object(pk)
        serializer = personaSerializer(persona)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        persona = self.get_object(pk)
        serializer = personaSerializer(persona, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        persona = self.get_object(pk)
        persona.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

''' Request and Responses
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

'''


@csrf_protect
def login_view(request):
    return render(request, "login.html", {})


def inicio_view(request):
    f = FormPersona(request.POST or None)
    if request.method == 'POST':
        if f.is_valid():
            datos = f.cleaned_data
            c = Persona()
            r = Rol()
            c.Rol = Rol
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
        "form": f,
    }
    return render(request, "inicio.html", {})


def reserva_view(request):
    return render(request, "reserva.html", {})


def servicio_view(request):
    return render(request, "servicios.html", {})
