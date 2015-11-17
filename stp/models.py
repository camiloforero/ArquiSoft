# -*- coding: utf-8 -*-

#Dentro de este archivo models.py se guarda la classinición de todas las clases del problema, con sus respectivos campos y las relaciones entre ellos. 
#Más información acerca de los modelos en https://docs.djangoproject.com/en/1.8/topics/db/models/
# Una descripción de cada uno de los campos se encuentra acá: https://docs.djangoproject.com/en/1.8/ref/models/fields/#model-field-types
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from authenticator.models import Perfil


class Vehiculo(models.Model):
    placa = models.CharField(primary_key=True, max_length=8)
    estado = models.CharField(max_length=16)
    ultimaRevision = models.DateTimeField(null=True)
    conductor = models.OneToOneField("Conductor", null=True)

class Conductor(Perfil):
    pass

class Usuario(Perfil):
    pass

class Mobibus(Vehiculo):
    pass

class EstacionVCub(models.Model):
    nombre = models.CharField(max_length=32)
    ubicacion = models.CharField(max_length=64)

class VCub(models.Model):
    estacion = models.ForeignKey(EstacionVCub, null=True, related_name="vcubs")
    usuario = models.ForeignKey(Usuario, null=True, related_name="vcubs")
    pass

class GPS(models.Model):
    imei = models.CharField(primary_key=True, max_length=64)
    mobibus = models.ForeignKey(Mobibus, null=True, related_name="dispositivos")

class EventoGPS(models.Model):
    tiempo = models.DateTimeField()
    tipo = models.CharField(max_length=16)#TODO: Hacer este campo un campo de opciones
    latitud = models.DecimalField(decimal_places=10, max_digits=14)
    longitud = models.DecimalField(decimal_places=10, max_digits=14)
    temperatura = models.DecimalField(decimal_places=3, max_digits=6)
    gps = models.ForeignKey(GPS)

class Tranvia(Vehiculo):
    pass

class Emergencia(models.Model):
    tiempo = models.DateTimeField()
    causa = models.CharField(max_length=16)
    reemplazo = models.BooleanField()
    tranvia = models.ForeignKey(Tranvia, related_name="emergencias")

# Create your models here.
