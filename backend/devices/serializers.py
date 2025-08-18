from rest_framework import serializers
from .models import MikrotikDevice

class MikrotikDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MikrotikDevice
        fields = '__all__'


