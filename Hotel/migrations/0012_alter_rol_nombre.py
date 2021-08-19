
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0011_pago_servicios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rol',
            name='Nombre',
            field=models.CharField(choices=[('Administrador', 'Administrador'), (
                'Cliente', 'Cliente')], default='Cliente', max_length=30),
        ),
    ]
