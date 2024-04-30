from .models import Restaurant, Menu_Items
from .serializers import RestaurantSerializer, MenuItemsSerializer
from .dal import RestaurantDAL, MenuDAL

class RestaurantService():
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.dal_inst = RestaurantDAL()
    
    def get_all_restaurants(self):
        restaurant_list = self.dal_inst.get_all_restaurants()
        serializer = RestaurantSerializer(restaurant_list,many=True)
        return serializer
    
    
    def get_restaurant_by_id(self, id):
        restaurant = self.dal_inst.get_restaurant_by_id(id)
        serializer = RestaurantSerializer(restaurant,many=False)
        return serializer
    
    
    def create_restaurant(self, data):
        serializer = RestaurantSerializer(data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            created_restaurant = self.dal_inst.create_restaurant(validated_data)
            return RestaurantSerializer(created_restaurant).data
        else:
            return None
        
    
    def update_restaurant(self, restaurant_id, data):
        serializer = RestaurantSerializer(data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            updated_restaurant = self.dal_inst.update_restaurant(restaurant_id, validated_data)
            return RestaurantSerializer(updated_restaurant).data
        else:
            return None
         
    def delete_restaurant(self, id):
        try:
            self.dal_inst.delete_restaurant(id)
            return True
        except Restaurant.DoesNotExist:
            return False
        

class MenuService:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.dal_inst = MenuDAL()
    
    def get_all_items(self):
        items = self.dal_inst.get_all_items()
        return MenuItemsSerializer(items, many=True)
    
    def get_item_by_restaurant_id(self, id):
        item = self.dal_inst.get_item_by_restaurant_id(id)
        return MenuItemsSerializer(item, many=True)
    
    def create_item(self, data, restaurant_id):

        data['restaurant'] = restaurant_id

        serialzer = MenuItemsSerializer(data = data)
        
        if serialzer.is_valid():
            validated_data = serialzer.validated_data
            
            created_item = self.dal_inst.create_item(validated_data)
            return MenuItemsSerializer(created_item).data
        else:
            return None
        
    def update_item(self, item_id, data):
        serializer = MenuItemsSerializer(data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            updated_item = self.dal_inst.update_item(item_id, validated_data)
            return MenuItemsSerializer(updated_item).data
        else:
            return None
        
    def delete_item(self, id):
        try:
            self.dal_inst.delete_items(id)
            return True
        except Menu_Items.DoesNotExist:
            return False
        

