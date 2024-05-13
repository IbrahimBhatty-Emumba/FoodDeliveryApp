import requests
from django.http import JsonResponse
from user.service import UserRoleService
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.urls import reverse
from django.template.response import TemplateResponse
from .auth_service import AuthService

class RBACMiddleware:

    def __init__(self, get_response):
        host = "project2"#'0.0.0.0'
        self.get_response = get_response
        self.auth_service = AuthService(host)

    def __call__(self, request):
        print("this is the middleware before jwt")
        if request.path == reverse('login_user'):
            return self.get_response(request)
        print("here")
        jwt_auth = JWTAuthentication()
        try:
           
            user, jwt_token = jwt_auth.authenticate(request)
            print(user, jwt_token)
            if user and jwt_token:

                role_id = jwt_token.payload.get('roles')  
                print("from jwt the role",role_id)
                request.role_id = role_id  
        except Exception as e:
            print("Error during JWT authentication:", e)
            return Response({'error': 'Invalid JWT token'}, status=status.HTTP_401_UNAUTHORIZED)
        
        # Call the process_request method
        response = self.process_request(request)
        print("this is the response after the process request method", response)

        if response is not None and not isinstance(response, TemplateResponse):
            # Check if response is already rendered and not None
            return response

        if response is not None:
            # Response is already a TemplateResponse, no need to create another one
            return response

        # If response is None, continue with the original response
        response = self.get_response(request)
        return response

    def process_request(self, request):
        # if request.path.startswith('/admin/'): 
        #     return None

        role_id = request.role_id 
        print("this is the role id", role_id)
        current_endpoint = request.path  
        print("this is the current endpoint", current_endpoint)

        permissions = UserRoleService.get_endpoints_for_role(role_id)

        print("these are the permissions", permissions)

        response_data = self.auth_service.check_permissions(permissions, current_endpoint)
        print("this is response data from the middleware", response_data)
        response_data = str(response_data)
        if response_data == "Unauthorized":
            return JsonResponse({'error': 'Unauthorized'}, status=403)
        elif response_data == "Authorized":
            return None  # Allow the request to continue
        else:
            # Handle unexpected response data
            return JsonResponse({'error': 'Unexpected response'}, status=500)




