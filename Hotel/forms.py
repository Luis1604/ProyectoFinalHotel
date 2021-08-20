from django import forms
from .models import Persona, Reserva, Pago

class FormPersona(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Persona
        fields=["cedula","Nombre","Apellido","Email","Telefono","Direccion","password"]

class FormReserva(forms.ModelForm):
    class Meta:
        model = Reserva
        fields=["numHabitacion","Persona","Fecha_Ingreso","Fecha_Caducidad"]

class FormPago(forms.ModelForm):
    class Meta:
        model = Pago
        fields=["Servicios","Habitacion"]

class FormLogin(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Persona
        fields=["Email","password"]

