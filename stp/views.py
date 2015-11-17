# -*- coding: utf-8 -*-
#En este archivo se guarda lo que en django se conoce como vistas; las maneras como se puede acceder a la información por detrás de la aplicación
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from stp.models import EventoGPS, Mobibus, GPS, VCub, EstacionVCub
from stp.serializers import EventoSerializer, MobibusSerializer, GPSSerializer, VCubSerializer, EstacionVCubSerializer, VCubAlquilerSerializer


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

class VCubList(generics.ListCreateAPIView):
    queryset = VCub.objects.all()
    serializer_class = VCubSerializer

class VCubDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VCub.objects.all()
    serializer_class = VCubSerializer

class EstacionVCubList(generics.ListCreateAPIView):
    queryset = EstacionVCub.objects.all()
    serializer_class = EstacionVCubSerializer

class EstacionVCubDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EstacionVCub.objects.all()
    serializer_class = EstacionVCubSerializer

class AlquilarVCub(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request, pk, format=None, pkvcub=None):
        if pkvcub is None:
            vcub = VCub.objects.filter(estacion=pk).first()
            vcub.estacion = None
            vcub.usuario = request.user.usuario
            vcub.save()
            return Response(VCubSerializer(vcub).data)
        else:
            vcub = VCub.objects.get(pk=pkvcub)
            vcub.estacion = EstacionVCub.objects.get(pk=pk)
            vcub.usuario = None
            vcub.save()
            return Response(VCubSerializer(vcub).data)

    
# Create your views here.
