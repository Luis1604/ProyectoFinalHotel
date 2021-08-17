from django import forms
from .models import Rol, Persona, Habitacion, RegistroHuespedes, Reserva, Servicios, Pago

class FormRol(forms.ModelForm):
    class Meta:
        model = Rol
        fields=["Nombre"]

class FormPersona(forms.ModelForm):
    class Meta:
        model = Persona
        fields=["Nombre","Apellido","cedula","Email","Telefono","password","Rol"]