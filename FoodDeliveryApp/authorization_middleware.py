import requests
from django.http import JsonResponse
from user.service import UserRoleService
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.urls import reverse
from django.template.response import TemplateResponse


class RBACMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("this is the middleware before jwt")
        if request.path == reverse('login_user'):
            return self.get_response(request)
        print("here")
        jwt_auth = JWTAuthentication()
        try:
            print(user, jwt_token)
            user, jwt_token = jwt_auth.authenticate(request)
            if user and jwt_token:

                role_id = jwt_token.payload.get('role')  
                print("from jwt the role",role_id)
                request.role_id = role_id  
        except Exception as e:
            print("Error during JWT authentication:", e)
            return Response({'error': 'Invalid JWT token'}, status=status.HTTP_401_UNAUTHORIZED)
        
        # Call the process_request method
        response = self.process_request(request)
        if not isinstance(response, TemplateResponse):  # Check if response is already rendered
            response = TemplateResponse(request, response.template_name, response.context_data)

        if response is not None:
            return response

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

        response = requests.post('http://127.0.0.1:8001/rbac-service/check-permissions/', json={'permissions': permissions, 'endpoint': current_endpoint})

        if response.status_code == 200:
            return None  
        else:
            return JsonResponse({'error': 'Unauthorized'}, status=403)

