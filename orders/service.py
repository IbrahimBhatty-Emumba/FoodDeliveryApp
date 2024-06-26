from .serializer import OrdersSerializer, OrdersItemsM2MSerializer
from .dal import OrderDal
from delivery_driver.dal import DeliveryDriverDAL
from django.db import transaction

class OrderService():
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.dal_inst = OrderDal()
        self.driver_dal_inst = DeliveryDriverDAL()

    def get_total_cost(self, items_data):
        total_cost = 0.0
        try:
            for item in items_data:
                item_id = item.get('item_id')
                item_cost = self.dal_inst.get_item_cost(item_id)
                total_cost += float(item_cost)
        except Exception as e:
            print("An error occurred while fetching item cost:", e)
            # Handle the error gracefully or raise it if needed
        total_cost = round(total_cost, 2)
        return total_cost
    


    def create_items(self, order_id, items_data):
        items_serialized = []
        for item_data in items_data:
            item_id = item_data.get('item_id')  # Extract 'item_id' from each item_data dictionary
            if item_id is not None:
                item_serializer = OrdersItemsM2MSerializer(data={'order_id': order_id, 'item_id': item_id})
                if item_serializer.is_valid():
                    validated_item_data = item_serializer.validated_data
                    created_order_item = self.dal_inst.create_item_order_m2m(validated_item_data)
                    items_serialized.append(OrdersItemsM2MSerializer(created_order_item).data)
                else:
                    print("Serializer errors:", item_serializer.errors)
                    raise Exception("Invalid item serializer data")
            else:
                print("Item ID not found in item data:", item_data)
                raise Exception("Item ID not found in item data")
            
        return items_serialized
                        


    def create_order(self, request, userid):
        try:
            
            driver_id = self.driver_dal_inst.get_available_driver()
            if driver_id is None:
                raise Exception("No Available Drivers")
            #pass json in class to unmarshel
            order_data = request.data.get('order', {})
            items_data = request.data.get('items', [])
            
            total_cost = self.get_total_cost(items_data)

            restaurant_id = int(order_data.get('restaurant_id'))
            user = int(userid)
        
            mapped_order_data = {
                'total_cost': total_cost,
                'restaurant': restaurant_id,  
                'user': user,  
                'delivery_driver': driver_id,  
            }
           
            with transaction.atomic():
                order_serializer = OrdersSerializer(data=mapped_order_data)

                if order_serializer.is_valid():
                    validated_order_data = order_serializer.validated_data
                    created_order = self.dal_inst.create_order(validated_order_data)
                    items_serialized = self.create_items(created_order.id,items_data)
                    serialized_order = OrdersSerializer(created_order).data

                    return {'order': serialized_order, 'items': items_serialized}

                else:
                    print("Serializer errors:", order_serializer.errors)
                    raise Exception("Invalid order serializer data")
        except Exception as e:
            # Log the exception or handle it as needed
            raise e
    
    def order_is_completed(self, id):
        try:
            with transaction.atomic():
                order =  self.dal_inst.order_is_completed(id)
                if order is None:
                    raise Exception
                driver_id = order.delivery_driver.driver_id
                print(driver_id)
                is_updated = self.driver_dal_inst.free_up_driver(driver_id)
                if is_updated:
                    return True
                else:
                    raise Exception("Not Found")

        except Exception as e:
            raise e

    