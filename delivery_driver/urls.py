from django.urls import path
from .views import (
    DeliveryDriverApiView,
)

urlpatterns = [
    path('<int:id>/', DeliveryDriverApiView.as_view(), name="delete_deliverydriver"),
    path('', DeliveryDriverApiView.as_view(), name="update_deliverydriver"),
    path('', DeliveryDriverApiView.as_view(), name="create_deliverydriver"),
    path('<int:id>/', DeliveryDriverApiView.as_view(), name="get_deliverydriver_by_id"),
    path('', DeliveryDriverApiView.as_view(), name="get_deliverydriver"),
]
