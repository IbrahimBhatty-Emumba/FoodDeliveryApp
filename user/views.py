from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework_simplejwt.tokens import Token, RefreshToken
from .service import UserService, UserRoleService

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

        user = self.service_inst.authenticate_user(email, password)

        user_role = self.service_inst.get_user_role(user.id)
        role_id = user_role.id
        if user:
          
            refresh_token = RefreshToken.for_user(user)

            
            print(refresh_token)
            payload = {
                'refresh': str(refresh_token),
                'access': str(refresh_token.access_token),
                'role':role_id
            }
            return Response(payload)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class RolesApiView(APIView):
    def __init__(self):
        self.service_inst = UserRoleService()
    
    def get(self, request, *args, **kwargs):
        roles = self.service_inst.get_all_roles()
        return Response(roles.data)
    
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            role = self.service_inst.create_new_role(data)
            if role:
                return Response(role, status=status.HTTP_201_CREATED)
            else:
                return Response("Invalid Data", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response("Internal Server Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class PermissionsApiView(APIView):
    def __init__(self):
        self.service_inst = UserRoleService()

    def get(self, request, *args, **kwargs):
         
        if(request.query_params.get("id")):
            id = int(request.query_params.get("id"))
            role_permissions = self.service_inst.get_role_permissions(id)
            return Response(role_permissions.data)
        else:
            permissions = self.service_inst.get_all_permissions()
            return Response(permissions.data)
    
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            created_permission = self.service_inst.create_new_permissions(data)
            if created_permission:
                return Response(created_permission, status=status.HTTP_201_CREATED)
            else:
                return Response("Invalid Data", status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response("Internal Server Error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

