from django.contrib import admin
from .models import Rol, Persona, Habitacion, RegistroHuespedes, Reserva, Servicios, Pago

class AdminRol(admin.ModelAdmin):
    list_display = ["__str__","Nombre"]
    class Meta(object):
        model = Rol

admin.site.register(Rol,AdminRol)

class AdminPersona(admin.ModelAdmin):
    list_display = ["__str__","Nombre","Apellido","cedula","Email","Direccion","password","Rol"]
    class Meta(object):
        model = Persona

admin.site.register(Persona,AdminPersona)

class AdminHabitacion(admin.ModelAdmin):
    list_display = ["__str__","numHabitacion","Tipo","numPiso","Detalle","Precio","Estado"]
    class Meta(object):
        model = Habitacion

admin.site.register(Habitacion,AdminHabitacion)

class AdminReserva(admin.ModelAdmin):
    list_display = ["__str__","Persona","numHabitacion","numReserva","Fecha_Ingreso","Fecha_Caducidad"]
    class Meta(object):
        model = Reserva

admin.site.register(Reserva,AdminReserva)

class AdminRegistroHuespedes(admin.ModelAdmin):
    list_display = ["__str__","Reserva","numPersonas","Fecha_Llegada","Fecha_Salida","Estado"]
    class Meta(object):
        model = RegistroHuespedes

admin.site.register(RegistroHuespedes,AdminRegistroHuespedes)

class AdminServicios(admin.ModelAdmin):
    list_display = ["__str__","Cliente","Nombre_Servicio","Precio","Descripcion","Estado"]
    class Meta(object):
        model = Servicios

admin.site.register(Servicios,AdminServicios)

class AdminPago(admin.ModelAdmin):
    list_display = ["__str__","Habitacion","Nombre","cedula","Detalle","Total"]
    class Meta(object):
        model = Pago

admin.site.register(Pago,AdminPago)