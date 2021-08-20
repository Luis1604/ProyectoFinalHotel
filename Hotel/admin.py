from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models import Rol, Persona, Habitacion, RegistroHuespedes, Reserva, Servicios, Pago
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

class AdminRol(admin.ModelAdmin):
    list_display = ["__str__", "Nombre"]

    class Meta(object):
        model = Rol


admin.site.register(Rol, AdminRol)


class AdminPersona(admin.ModelAdmin):
    list_display = ["__str__", "Nombre", "Apellido",
                    "cedula", "Email", "Direccion", "password", "Rol"]
    list_filter = ["Nombre", "Apellido", "cedula", "Email", "Rol"]

    class Meta(object):
        model = Persona

admin.site.register(Persona)


class AdminHabitacion(admin.ModelAdmin):
    list_display = ["__str__", "numHabitacion", "Tipo",
                    "numPiso", "Detalle", "Precio", "Estado"]
    list_filter = ["numHabitacion", "Tipo", "numPiso", "Estado"]

    class Meta(object):
        model = Habitacion

admin.site.register(Habitacion, AdminHabitacion)


class AdminReserva(admin.ModelAdmin):
    list_display = ["__str__", "Persona", "numHabitacion",
                    "Fecha_Ingreso", "Fecha_Caducidad"]
    list_filter = ["Persona", "numHabitacion",
                   "Fecha_Ingreso", "Fecha_Caducidad"]

    class Meta(object):
        model = Reserva


admin.site.register(Reserva, AdminReserva)


class AdminRegistroHuespedes(admin.ModelAdmin):
    list_display = ["__str__", "Reserva", "numPersonas",
                    "Fecha_Llegada", "Fecha_Salida", "Estado"]
    list_filter = ["Reserva", "Fecha_Llegada", "Fecha_Salida", "Estado"]

    class Meta(object):
        model = RegistroHuespedes


admin.site.register(RegistroHuespedes, AdminRegistroHuespedes)


class AdminServicios(admin.ModelAdmin):
    list_display = ["__str__", "Nombre_Servicio", "Precio",
                    "Descripcion"]
    list_filter = ["Nombre_Servicio", "Precio",
                    "Descripcion"]

    class Meta(object):
        model = Servicios


admin.site.register(Servicios, AdminServicios)


class AdminPago(admin.ModelAdmin):
    list_display = ["__str__", "Habitacion",
                    "Nombre", "cedula", "Detalle", "Total"]
    list_filter = ["Habitacion", "Nombre", "cedula"]

    class Meta(object):
        model = Pago


admin.site.register(Pago, AdminPago)
