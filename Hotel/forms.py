from django import forms
from .models import Persona, Reserva

class FormPersona(forms.ModelForm):
    class Meta:
        model = Persona
        fields=["Nombre","Apellido","cedula","Email","Telefono","Direccion","password","Rol"]

class FormReserva(forms.ModelForm):
    class Meta:
        model = Reserva
        fields=["Persona","numReserva","numHabitacion","Fecha_Ingreso","Fecha_Caducidad"]

