
from rest_framework import serializers
from stp.models import EventoGPS, Mobibus, GPS, VCub, EstacionVCub


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoGPS
        fields = ('id', 'tiempo', 'tipo', 'latitud', 'longitud', 'temperatura')

class MobibusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobibus
        fields = ('placa', 'ultimaRevision', 'estado')

class GPSSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPS
        fields = ('imei', 'mobibus')

class VCubSerializer(serializers.ModelSerializer):
    class Meta:
        model = VCub 
        fields = ('id', 'estacion', 'usuario')

class EstacionVCubSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstacionVCub 
        fields = ('nombre', 'ubicacion')

class VCubAlquilerSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    vcub = serializers.IntegerField()
