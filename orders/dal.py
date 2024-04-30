from .models import Orders, OrdersItemsM2M

class OrderDal:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    #unit of work?
    def create_order(self, order_data):
        order_instance = Orders.objects.create(**order_data)
        return order_instance
    
    def create_item_order_m2m(self, item_data):
        item_instance = OrdersItemsM2M.objects.create(**item_data)
        return item_instance
    
    def order_is_completed(self, id):
        order_instance = Orders.objects.get(pk = id)
        order_instance.is_completed = True
        order_instance.save()
        print("this is the order instance", order_instance)
        return order_instance