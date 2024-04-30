from rest_framework import serializers
from .models import Restaurant, Menu_Items

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["restaurant_id","owner","restaurant_name","created_date", "address"]


class MenuItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu_Items
        fields = ["id","restaurant","name","cost","description","created_date"]