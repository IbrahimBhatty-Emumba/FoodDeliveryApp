from rest_framework import serializers
from .models import DeliveryDrivers

class DeliveryDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryDrivers
        fields = ["driver_id","driver_name","is_avaliable","created_date"]