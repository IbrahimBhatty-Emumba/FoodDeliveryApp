from .models import DeliveryDrivers

class DeliveryDriverDAL:
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_all_drivers(self):
        return DeliveryDrivers.objects.all()
    
    
    def get_driver_by_id(self, id):
        driver = DeliveryDrivers.objects.get(pk = id)
        if driver is None:
            return None
        else:
            return driver
    

    def get_available_driver(self):
        try:
            driver = DeliveryDrivers.objects.filter(is_avaliable=True).first()
            if driver:
                driver.is_avaliable = False
                driver.save()
                print(driver.driver_id)
                return driver.driver_id
            else:
                return None
        except Exception as e:
            raise e
    
    def free_up_driver(self, id):
        try:
            driver = DeliveryDrivers.objects.get(pk=id)
            driver.is_avaliable = True
            driver.save()
            return True
        except Exception as e:
            raise e

    def create_driver(self, validated_data):
        print(validated_data)
        return DeliveryDrivers.objects.create(**validated_data)
    
    
    def update_driver(self, id, validated_data):
        try:
            driver = DeliveryDrivers.objects.get(pk=id)

            for key,value in validated_data.items():
                setattr(driver,key,value)
            driver.save()
            return driver
        except DeliveryDrivers.DoesNotExist:
            return None
        
    
    def delete_driver(self, id):
        driver =  DeliveryDrivers.objects.get(pk=id)
        driver.delete()