from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework_simplejwt.tokens import Token, RefreshToken
from .service import UserService

class UserApiView(APIView):
      
    def __init__(self):
        self.service_inst = UserService()
    
    def get(self, request, *args, **kwargs):
         
        if(request.query_params.get("id")):
            id = int(request.query_params.get("id"))
            user = self.service_inst.get_user_by_id(id)
            return Response(user.data)
        else:
            users = self.service_inst.get_all_users()
            return Response(users.data)
        
    def post(self, request, *args, **kwargs):
        data = request.data
        #print(data)
        created_user = self.service_inst.register_user(data)
        print(created_user)
        if created_user:
            return Response(created_user, status=status.HTTP_200_OK)
        else:
            return Response("Invalid Data", status=status.HTTP_400_BAD_REQUEST)
        

class LoginApiView(APIView):
    def __init__(self):
        self.service_inst = UserService()
    
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        # print(email,password)
        user = self.service_inst.authenticate_user(email, password)
        print(user)
        print("from login")
        if user:
            # access_token = Token.for_user(user)
            # print(access_token)
            # Generate refresh token
            refresh_token = RefreshToken.for_user(user)

            # Now you can print or return the tokens
            # print(access_token)
            print(refresh_token)
            payload = {
                'refresh': str(refresh_token),
                'access': str(refresh_token.access_token),
            }
            return Response(payload)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
