# Generated by Django 3.2.4 on 2021-08-17 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0008_registrohuespedes_numregistro'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='numPago',
            field=models.CharField(default='', max_length=10),
        ),
    ]
