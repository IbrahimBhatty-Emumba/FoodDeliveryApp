from django.urls import path
from .views import (
    OrderApiView
)

urlpatterns = [
    path('create-order/', OrderApiView.as_view(), name="create_order"),
    path('update-order/<int:id>/', OrderApiView.as_view(), name="update-order"),

]