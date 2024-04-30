from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .service import RestaurantService, MenuService

class RestaurantApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def __init__(self):
        self.service_inst = RestaurantService()

    def get(self, request,*args, **kwargs):
        if(request.query_params.get("id")):
            id = int(request.query_params.get("id"))
            restaurant = self.service_inst.get_restaurant_by_id(id)
            return Response(restaurant.data)
        else:
            restaurants = self.service_inst.get_all_restaurants()
            return Response(restaurants.data)
         
    def post(self, request,*args, **kwargs):
        data = request.data
        owner_id = request.user.id
        data["owner"] = owner_id
        print(data)
        created_restaurant = self.service_inst.create_restaurant(data)

        if created_restaurant:
            return Response(created_restaurant, status=status.HTTP_201_CREATED)
        else:
            return Response("Invalid Data", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,*args, **kwargs):
        data = request.data
        restaurant_id = request.data.get('restaurant_id')
        if restaurant_id is None:
            return Response("Restaurant ID not provided", status=status.HTTP_400_BAD_REQUEST)
        
        updated_restaurant = self.service_inst.update_restaurant(restaurant_id, data)

        if updated_restaurant:
            return Response(updated_restaurant, status=status.HTTP_200_OK)
        else:
            return Response("Resataurant Does Not Exist", status=status.HTTP_400_OK)

    def delete(self, request, id):
        delete_req = self.service_inst.delete_restaurant(id)
        if delete_req:
            return Response("Deletion Successfull", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("Restaurant not found", status=status.HTTP_400_BAD_REQUEST)



class MenuItemApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def __init__(self):
        self.service_inst = MenuService()
    
    def get(self, request, restaurant_id, *args, **kwargs):
        if(restaurant_id):
            id = int(restaurant_id)
            
            items = self.service_inst.get_item_by_restaurant_id(id)
            return Response(items.data)
        else:
            items = self.service_inst.get_all_items()
            return Response(items.data)
    
    def post(self, request, restaurant_id):

        data = request.data.copy()
        id = restaurant_id
       
        created_item = self.service_inst.create_item(data, id)

        if created_item:
            return Response(created_item, status=status.HTTP_201_CREATED)
        else:
            return Response("Invalid Data", status=status.HTTP_400_BAD_REQUEST)


