"""
URL configuration for FoodDeliveryApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path, include
from customer import urls as customer_urls
from restaurant import urls as restaurant_urls
from delivery_driver import urls as driver_urls
from user import urls as user_urls
from orders import urls as order_urls

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('customer/', include(customer_urls)),
    path('restaurant/', include(restaurant_urls)), 
    path('deliverydriver/',include(driver_urls)),
    path('user/',include(user_urls)),
    path('user/<int:userid>/orders/',include(order_urls)),
]
