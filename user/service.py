from django.contrib.auth import authenticate
from .dal import UserDAL, RolesAndPermissionDAL
from .serializer import UserSerializer, RoleSerializer, PermissionSerializer, RolesPermissionsM2mSerializer

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
    
    def get_user_role(self, user_id):
        role = self.dal_inst.get_user_role(user_id)
        return role

class UserRoleService:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.dal_inst = RolesAndPermissionDAL()

    def get_all_roles(self):
        roles = self.dal_inst.get_all_roles()
        return RoleSerializer(roles, many=True)
    
    def get_all_permissions(self):
        permissions = self.dal_inst.get_all_permission()
        return PermissionSerializer(permissions, many=True)
    
    def get_role_permissions(self, request):
        id = request.get("role_id")
        permissions = self.dal_inst.get_role_permissions(id)
        return PermissionSerializer(permissions, many=True)
    
    def create_new_permissions(self, request):
        serializer = PermissionSerializer(data = request)
        if serializer.is_valid():
            created_permission = self.dal_inst.create_new_permission(serializer.validated_data)
            return PermissionSerializer(created_permission).data
        else:
            return None
        
    def create_new_role(self, request):
        role_data =  request.get("role_data")
        permissions_data = request.get("permission_data")
        print(permissions_data)
        role_serializer = RoleSerializer(data=role_data)
        if role_serializer.is_valid():
            created_role = self.dal_inst.create_new_role(role_serializer.validated_data)
            # print(RoleSerializer(created_role).data)
            serialized_m2m = []
            for permission in permissions_data:
                permission_id = permission.get("id")
                if permission_id is not None:

                    m2mserializer = RolesPermissionsM2mSerializer(data={'role': created_role.id, 'permission': permission_id})
                    if m2mserializer.is_valid():
                        created_m2m_object = self.dal_inst.create_m2m_object(m2mserializer.validated_data)
                        serialized_m2m.append(RolesPermissionsM2mSerializer(created_m2m_object).data)
                        # print(RolesPermissionsM2mSerializer(created_m2m_object).data)
                    else:
                        print("Serializer errors:", m2mserializer.errors)
                        raise Exception("Invalid item serializer data")
                else:
                    print("Permission ID not found in data:", permissions_data)
                    raise Exception("Permission ID not found in data")
                
              
            serialized_role = RoleSerializer(created_role).data
            return {'role': serialized_role, 'permissions': serialized_m2m}  
            
        else:
            print("Serializer errors:", role_serializer.errors)
            raise Exception("Invalid role serializer data")

