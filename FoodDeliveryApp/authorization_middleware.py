# authorization_middleware.py

from django.conf import settings
from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication

class AuthorizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the authorization header from the request
        authorization_header = request.headers.get('Authorization')

        # Check if the authorization header exists and starts with 'Bearer '
        if authorization_header and authorization_header.startswith('Bearer '):
            # Extract the token from the header
            token = authorization_header.split(' ')[1]

            # Verify the token using Simple JWT
            jwt_authentication = JWTAuthentication()
            try:
                user, _ = jwt_authentication.authenticate(request)
                request.user = user
            except Exception as e:
                return JsonResponse({"error": "Invalid token"}, status=401)

        # Call the next middleware or view
        response = self.get_response(request)
        return response
