# -*- coding: utf-8 -*-
#En este archivo se guarda lo que en django se conoce como vistas; las maneras como se puede acceder a la información por detrás de la aplicación
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from stp.models import EventoGPS, Mobibus, GPS
from stp.serializers import EventoSerializer, MobibusSerializer, GPSSerializer


class MobibusList(generics.ListCreateAPIView):
    queryset = Mobibus.objects.all()
    serializer_class = MobibusSerializer

class MobibusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mobibus.objects.all()
    serializer_class = MobibusSerializer

class GPSList(generics.ListCreateAPIView):
    queryset = GPS.objects.all()
    serializer_class = GPSSerializer

class GPSDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GPS.objects.all()
    serializer_class = GPSSerializer

class EventoList(generics.ListCreateAPIView):
    def get_queryset(self):
        gps_pk = self.kwargs['gps_pk']
        return EventoGPS.objects.filter(gps = gps_pk)
    serializer_class = EventoSerializer
# Create your views here.
