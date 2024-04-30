from .models import Restaurant, Menu_Items

class RestaurantDAL:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_all_restaurants(self):
        return Restaurant.objects.all()
    

    def get_restaurant_by_id(self, id):
        return Restaurant.objects.get(restaurant_id = id)
    
    
    def create_restaurant(self, validated_data):
        return Restaurant.objects.create(**validated_data)
    
    
    def update_restaurant(self, restaurant_id, validated_data):
        try:
            restaurant = Restaurant.objects.get(pk = restaurant_id)
            for key, value in validated_data.items():
                setattr(restaurant, key, value)
            restaurant.save()
            return restaurant
        except Restaurant.DoesNotExist:
            return None
        

    
    def delete_restaurant(self, restaurant_id):
        restaurant = Restaurant.objects.get(pk=restaurant_id)
        restaurant.delete()


class MenuDAL:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_all_items(self):
       
        return Menu_Items.objects.all()
    
    def get_item_by_restaurant_id(self, id):
        
        return Menu_Items.objects.filter(restaurant = id)
    
    def create_item(self, validated_data):
        return Menu_Items.objects.create(**validated_data)
    
    def update_item(self, item_id, validated_data):
        try:
            item = Menu_Items.objects.get(pk = item_id)
            for key,value in validated_data.items():
                setattr(item, key, value)
            item.save()
            return item
        except Menu_Items.DoesNotExist:
            return None
        
    def delete_items(self, item_id):
        item = Restaurant.objects.get(pk=item_id)
        item.delete()
    
        