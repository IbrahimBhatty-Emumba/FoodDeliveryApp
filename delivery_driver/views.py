from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .services import DeliveryDriverService

class DeliveryDriverApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def __init__(self):
        self.service_inst = DeliveryDriverService()

    def get(self, request, *args, **kwargs):

        if(request.query_params.get("id")):
            id = int(request.query_params.get("id"))
            driver = self.service_inst.get_driver_by_id(id)
            return Response(driver.data)
        else:
            drivers = self.service_inst.get_all_drivers()
            return Response(drivers.data)
        
    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        created_driver = self.service_inst.create_driver(data)

        if created_driver:
            return Response(created_driver, status=status.HTTP_200_OK)
        else:
            return Response("Invalid Data", status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):
        data = request.data
        driver_id = request.data.get('driver_id')

        if driver_id is None:
            return Response("Driver ID not provided", status=status.HTTP_400_BAD_REQUEST)
        
        updated_driver = self.service_inst.update_driver(driver_id, data)

        if updated_driver:
            return Response(updated_driver, status=status.HTTP_200_OK)
        else:
            return Response("Driver does not exist", status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        delete_req = self.service_inst.delete_driver(id)

        if delete_req:
            return Response("Deletion Successful", status=status.HTTP_200_OK)
        else:
            return Response("Driver not found", status=status.HTTP_401_NOT_FOUND)
        
             
    


