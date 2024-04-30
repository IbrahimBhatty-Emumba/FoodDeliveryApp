from django.urls import path
from .views import (
    RestaurantApiView,
    MenuItemApiView
)

urlpatterns = [
    path('<int:restaurant_id>/items/', MenuItemApiView.as_view(), name="create_item"),
    path('<int:restaurant_id>/items/', MenuItemApiView.as_view(), name="get_items_by_restaurant_id"),
    path('items/', MenuItemApiView.as_view(), name="get_items"),
    path('<int:id>/', RestaurantApiView.as_view(), name="delete_restaurant"),
    path('', RestaurantApiView.as_view(), name="update_restaurant"),
    path('', RestaurantApiView.as_view(), name="create_restaurant"),
    path('<int:id>/', RestaurantApiView.as_view(), name="get_restaurant_by_id"),
    path('', RestaurantApiView.as_view(), name="get_restaurant"),
]
