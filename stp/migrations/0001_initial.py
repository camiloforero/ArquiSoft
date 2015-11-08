# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('nombres', models.CharField(max_length=32)),
                ('apellidos', models.CharField(max_length=32)),
                ('cedula', models.CharField(max_length=32, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Emergencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tiempo', models.DateTimeField()),
                ('causa', models.CharField(max_length=16)),
                ('reemplazo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='EventoGPS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tiempo', models.DateTimeField()),
                ('tipo', models.CharField(max_length=16)),
                ('latitud', models.DecimalField(max_digits=14, decimal_places=10)),
                ('longitud', models.DecimalField(max_digits=14, decimal_places=10)),
                ('temperatura', models.DecimalField(max_digits=6, decimal_places=3)),
            ],
        ),
        migrations.CreateModel(
            name='GPS',
            fields=[
                ('imei', models.CharField(max_length=64, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('placa', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('ultimaRevision', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mobibus',
            fields=[
                ('vehiculo_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='stp.Vehiculo')),
            ],
            bases=('stp.vehiculo',),
        ),
        migrations.CreateModel(
            name='Tranvia',
            fields=[
                ('vehiculo_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='stp.Vehiculo')),
            ],
            bases=('stp.vehiculo',),
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='conductor',
            field=models.OneToOneField(null=True, to='stp.Conductor'),
        ),
    ]
