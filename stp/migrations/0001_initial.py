# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('cedula', models.CharField(max_length=32)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('user', models.OneToOneField(related_name='conductor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
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
            name='EstacionVCub',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=32)),
                ('ubicacion', models.CharField(max_length=64)),
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
            name='VCub',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estacion', models.ForeignKey(related_name='vcubs', to='stp.EstacionVCub', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('placa', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('estado', models.CharField(max_length=16)),
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
        migrations.AddField(
            model_name='eventogps',
            name='gps',
            field=models.ForeignKey(to='stp.GPS'),
        ),
        migrations.AddField(
            model_name='gps',
            name='mobibus',
            field=models.ForeignKey(related_name='dispositivos', to='stp.Mobibus', null=True),
        ),
        migrations.AddField(
            model_name='emergencia',
            name='tranvia',
            field=models.ForeignKey(related_name='emergencias', to='stp.Tranvia'),
        ),
    ]
