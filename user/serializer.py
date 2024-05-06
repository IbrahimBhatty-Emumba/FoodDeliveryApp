from rest_framework import serializers
import re
from .models import Users, Roles, Permissions, Role_Permission_M2M

class UserSerializer(serializers.ModelSerializer):

    # Id = serializers.IntegerField(required=False)

    class Meta: 
        model = Users
        fields = [ "name", "email", "password", "type", "role", "address", "phone", "created_date"]  
        # exclude = ["Id"]
    
    def validate(self, attrs):
        errors = {}

        name = attrs.get("name")
        if name and any(char.isdigit() for char in name):
            errors["name"] = ["Name cannot contain numbers"]

        email = attrs.get("email")
        if email:
            if not re.match(r'^.+@[^.].*\.[a-zA-Z]{2,}$', email):
                errors["email"] = ["Invalid email format"]
        
        password = attrs.get("password")
        if password:
            if len(password) < 8:
                errors["password"] = ["Password must be at least 8 characters long"]

            if not re.match(r'^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_+{}|:"<>?]).{8,}$', password):
                errors["password"] = ["Password must contain at least one uppercase letter, one number, and one special character"]
        
        type = attrs.get("type")
        if type:
            if type not in ["customer", "admin"]:
                errors["type"]=["Incorrect type"]

        address = attrs.get("address")
        if address:
            if len(address) < 5:
                errors["address"] = ["Address must be atleast 5 characters long"]

        phone = attrs.get("phone")
        if phone:
            if not 11 <= len(phone) <= 13:
                errors["phone"] = ["Phone number must be between 11 and 13 characters long"]

            if not re.match(r'^\+?[0-9]+$', phone):
                errors["phone"] = ["Phone number must contain only numbers and may start with a '+'"]



    
        if errors:
            raise serializers.ValidationError(errors)

        return attrs
    

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ["id","label"]
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissions
        fields = ["id","label","endpoint"]
class RolesPermissionsM2mSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role_Permission_M2M
        fields = ["id","role","permission"]