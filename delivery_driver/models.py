from django.db import models

class DeliveryDrivers(models.Model):
    driver_id = models.AutoField(primary_key=True)
    driver_name = models.CharField(max_length=50, blank=True, null=True)
    is_avaliable = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'delivery_drivers'