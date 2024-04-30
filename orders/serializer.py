from rest_framework import serializers
from .models import Orders, OrdersItemsM2M

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['total_cost', 'restaurant', 'user', 'delivery_driver']

class OrdersItemsM2MSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdersItemsM2M
        fields = ['id', 'order_id', 'item_id']