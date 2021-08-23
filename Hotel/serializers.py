from rest_framework import fields, serializers
from .models import Persona, Rol, Habitacion, Reserva, RegistroHuespedes, Servicios, Pago


class rolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['Administrador', 'Cliente']


class personaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id', 'Rol', 'cedula', 'Nombre', 'Apellido',
                  'Email', 'Telefono', 'Direccion', 'password']


class habitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = ['id', 'numHabitacion', 'Tipo',
                  'numPiso', 'Detalle', 'Precio', 'Estado']


class reservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id', 'Persona', 'numReserva',
                  'numHabitacion', 'Fecha_Ingreso', 'Fecha_Caducidad']


class registroHuespedesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroHuespedes
        fields = ['id', 'Reserva', 'numPersonas',
                  'Fecha_Llegada', 'Fecha_Salida', 'Estado']


class serviciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicios
        fields = ['id', 'Nombre_Servicio', 'Precio', 'Descripcion']


class pagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ['Habitacion', 'Servicios', 'numPago', 'cedula',
                  'Nombre', 'Apellido', 'Email', 'Direccion', 'Detalle', 'Total', 'Estado']
