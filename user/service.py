from django.contrib.auth import authenticate
from .dal import UserDAL
from .serializer import UserSerializer

class UserService:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.dal_inst = UserDAL()

    def get_all_users(self):
        users = self.dal_inst.get_all_users()
        return UserSerializer(users, many=True)
    
    def get_user_by_id(self, id):
        user = self.dal_inst.get_user_by_id(id)
        return UserSerializer(user, many=False)
    
    def register_user(self, request):
        password = request.get("password")
        confirmed_password = request.get("confirmed_password")

        if password != confirmed_password:
            raise ValueError("Passwords do not match")

        serializer = UserSerializer(data=request)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            print(validated_data)
            created_user = self.dal_inst.register_user(validated_data)
            return UserSerializer(created_user).data
        else:
            return serializer.errors
    
    def authenticate_user(self, email, password):
        is_authenticated = self.dal_inst.authenticate_user(email, password)
        print(UserSerializer(is_authenticated).data)
        return is_authenticated