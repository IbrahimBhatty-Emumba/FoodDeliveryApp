from .models import Users

class UserDAL:

    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_all_Users(self):
        return Users.objects.all()
    
    def get_user_by_id(self, id):
        return Users.objects.get(pk=id)
    
    def register_user(self, validated_data):
        return Users.objects.create(**validated_data)
    
    def authenticate_user(self, email, password):
        user = Users.objects.get(email= email)
        print(user)
        if user.password == password:
            return user
        else:
            return None
    
