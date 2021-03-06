# Generated by Django 3.2.4 on 2021-08-15 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numHabitacion', models.IntegerField(default='', max_length=4)),
                ('Tipo', models.CharField(choices=[('Individual', 'Individual'), ('Doble', 'Doble'), ('Triple', 'Triple'), ('Suite', 'Suite')], default='Individual', max_length=30)),
                ('numPiso', models.IntegerField(default='', max_length=4)),
                ('Detalle', models.CharField(max_length=200)),
                ('Precio', models.DecimalField(decimal_places=2, max_digits=20)),
                ('Estado', models.CharField(choices=[('Disponible', 'Disponible'), ('Reservada', 'Reservada'), ('Ocupada', 'Ocupada')], default='Disponible', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=10)),
                ('Nombre', models.CharField(max_length=30)),
                ('Apellido', models.CharField(default='', max_length=30)),
                ('Email', models.EmailField(default='', max_length=30)),
                ('Telefono', models.CharField(default='', max_length=30)),
                ('Direccion', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(choices=[('Administrador', 'Administrador'), ('Ciente', 'Ciente')], default='Ciente', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Servicio', models.CharField(max_length=30)),
                ('Precio', models.DecimalField(decimal_places=2, max_digits=20)),
                ('Descripcion', models.CharField(max_length=200)),
                ('Estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Pagado', 'Pagado')], default='Pendiente', max_length=30)),
                ('Cliente', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Hotel.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha_Ingreso', models.DateField()),
                ('Fecha_Caducidad', models.DateField()),
                ('Persona', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Hotel.persona')),
                ('numHabitacion', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Hotel.habitacion')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroHuespedes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numPersonas', models.IntegerField(default='', max_length=4)),
                ('Fecha_Llegada', models.DateField()),
                ('Fecha_Salida', models.DateField()),
                ('Estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Pagado', 'Pagado')], default='Pendiente', max_length=30)),
                ('Habitacion', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Hotel.habitacion')),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='Rol',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Hotel.rol'),
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=10)),
                ('Nombre', models.CharField(max_length=30)),
                ('Apellido', models.CharField(default='', max_length=30)),
                ('Email', models.EmailField(default='', max_length=30)),
                ('Direccion', models.CharField(max_length=70)),
                ('DesDetallecripcion', models.CharField(max_length=200)),
                ('Total', models.DecimalField(decimal_places=2, max_digits=20)),
                ('Habitacion', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Hotel.registrohuespedes')),
            ],
        ),
    ]
