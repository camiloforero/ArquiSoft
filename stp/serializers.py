
from rest_framework import serializers
from stp.models import EventoGPS, Mobibus, GPS


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
