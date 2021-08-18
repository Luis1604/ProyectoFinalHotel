from rest_framework import fields, serializers
from .models import Persona, Rol


class personaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['id', 'Rol', 'cedula', 'Nombre',
                  'Apellido', 'Email', 'Telefono', 'Direccion', 'password']
