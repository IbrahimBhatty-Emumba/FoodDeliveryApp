from .serializer import DeliveryDriverSerializer
from .models import DeliveryDrivers
from .dal import DeliveryDriverDAL

class DeliveryDriverService:
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.dal_inst = DeliveryDriverDAL()
    
    def get_all_drivers(self):
        drivers = self.dal_inst.get_all_drivers()
        serializer = DeliveryDriverSerializer(drivers, many=True)
        return serializer
    
    def get_driver_by_id(self, id):
        driver = self.dal_inst.get_driver_by_id(id)
        serializer = DeliveryDriverSerializer(driver, many=False)
        return serializer
    
    def create_driver(self, data):
        serializer= DeliveryDriverSerializer(data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            print(validated_data)
            created_driver = self.dal_inst.create_driver(validated_data)
            return DeliveryDriverSerializer(created_driver).data
        else:
            return None
    
    def update_driver(self, id, data):
        serializer = DeliveryDriverSerializer(data=data)

        if serializer.is_valid():
            validated_data = serializer.validated_data
            updated_driver = self.dal_inst.update_driver(id,validated_data)
            return DeliveryDriverSerializer(updated_driver).data
        else:
            return None
        
    def delete_driver(self, id):
        try:
             self.dal_inst.delete_driver(id)
             return True
        except DeliveryDrivers.DoesNotExist:
            return False