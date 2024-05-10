from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .service import OrderService
from django.db import transaction

class OrderApiView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def __init__(self):
        self.service_inst = OrderService()

    @transaction.atomic
    def post(self, request, userid, *args, **kwargs):
        try:
            print("this is the request to create an order", request)

            created_order = self.service_inst.create_order(request, userid)


            if created_order:
                return Response(created_order, status=status.HTTP_201_CREATED)
            else:
                return Response("Invalid Data", status=status.HTTP_400_BAD_REQUEST)
    
        except Exception as e:
            #make custom validation
            if str(e) == "No Available Drivers":
                return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response("Internal Server Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    @transaction.atomic
    def put(self, request, id, userid):
        try:
            entires_updated = self.service_inst.order_is_completed(id)
            if entires_updated:
                 return Response("Updated status", status=status.HTTP_200_OK)
            else:
                return Response("Not Found", status=status.HTTP_400_BAD_REQUEST)
    


        except Exception as e:
            return Response("Internal Server Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

