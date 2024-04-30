from django.db import models
from user.models import Users
from restaurant.models import Restaurant, Menu_Items
from delivery_driver.models import DeliveryDrivers

class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(auto_created=True, default=False)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    delivery_driver = models.ForeignKey(DeliveryDrivers, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) 


class OrdersItemsM2M(models.Model):
    id = models.AutoField(primary_key=True)
    order_id =  models.ForeignKey(Orders, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Menu_Items, on_delete=models.CASCADE)