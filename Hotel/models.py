from django.db import models
# creando

class Rol(models.Model):

    Nombre = models.CharField(max_length=30, choices=(
        ('Administrador', ("Administrador")), ('Cliente', ("Cliente"))), default='Cliente')

    def __str__(self):
        return self.Nombre

class Persona(models.Model):

    Rol = models.ForeignKey(Rol(), on_delete=models.CASCADE, default="")
    cedula = models.CharField(max_length=10, blank=False)
    Nombre = models.CharField(max_length=30, blank=False)
    Apellido = models.CharField(max_length=30, blank=False, default='')
    Email = models.EmailField(max_length=30, blank=False, default='')
    Telefono = models.CharField(max_length=30, blank=False, default='')
    Direccion = models.CharField(max_length=70, blank=False)
    password = models.CharField(max_length=20, blank=False)
        
    def __str__(self):
        return "%s %s" % (self.Nombre, self.Apellido)

class Habitacion(models.Model):

    numHabitacion = models.CharField(max_length=6, blank=False, default='')
    Tipo = models.CharField(max_length=30, choices=(('Individual', ("Individual")), (
        'Doble', ("Doble")), ('Triple', ("Triple")), ('Suite', ("Suite"))), default='Individual')
    numPiso = models.IntegerField(blank=False, default='')
    Detalle = models.CharField(max_length=200, blank=False)
    Precio = models.DecimalField(max_digits=20, decimal_places=2, blank=False)
    Estado = models.CharField(max_length=30, choices=(('Disponible', ("Disponible")), (
        'Reservada', ("Reservada")), ('Ocupada', ("Ocupada"))), default='Disponible')

    def __str__(self):
        return self.numHabitacion


class Reserva(models.Model):

    Persona = models.ForeignKey(
        Persona(), on_delete=models.CASCADE, default="")
    numReserva = models.CharField(max_length=10, blank=False, default='')
    numHabitacion = models.ForeignKey(
        Habitacion(), on_delete=models.CASCADE, default="")
    Fecha_Ingreso = models.DateField(blank=False)
    Fecha_Caducidad = models.DateField(blank=False)

    def __str__(self):
        return self.numReserva


class RegistroHuespedes(models.Model):
    Reserva = models.ForeignKey(
        Reserva(), on_delete=models.CASCADE, default="")
    numPersonas = models.IntegerField(blank=False, default='')
    Fecha_Llegada = models.DateField(blank=False)
    Fecha_Salida = models.DateField(blank=False)
    Estado = models.CharField(max_length=30, choices=(
        ('Pendiente', ("Pendiente")), ('Pagado', ("Pagado"))), default='Pendiente')

    def __str__(self):
        return self.Reserva.numHabitacion.numHabitacion


class Servicios(models.Model):

    Nombre_Servicio = models.CharField(max_length=30, blank=False)
    Precio = models.DecimalField(max_digits=20, decimal_places=2, blank=False)
    Descripcion = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.Nombre_Servicio


class Pago(models.Model):

    Habitacion = models.ForeignKey(
        RegistroHuespedes(), on_delete=models.CASCADE, default="")
    Servicios = models.ForeignKey(
        Servicios(), on_delete=models.CASCADE, default="")
    numPago = models.CharField(max_length=10, blank=False, default='')
    cedula = models.CharField(max_length=10, blank=False)
    Nombre = models.CharField(max_length=30, blank=False)
    Apellido = models.CharField(max_length=30, blank=False, default='')
    Email = models.EmailField(max_length=30, blank=False, default='')
    Direccion = models.CharField(max_length=70, blank=False)
    Detalle = models.CharField(max_length=200, blank=False)
    Total = models.DecimalField(max_digits=20, decimal_places=2, blank=False)
    Estado = models.CharField(max_length=30, choices=(
        ('Pendiente', ("Pendiente")), ('Pagado', ("Pagado"))), default='Pendiente')

    def __str__(self):
        return self.Habitacion.Reserva.numHabitacion.numHabitacion
