from .models import Users, Roles, Permissions, Role_Permission_M2M

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
    
    def get_user_role(self, user_id):
        user_obj = Users.objects.get(pk=user_id)
        role = user_obj.role

        return role

class RolesAndPermissionDAL:
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_all_roles(self):
        return Roles.objects.all()
    
    def get_all_permission(self):
        return Permissions.objects.all()
    
    def get_role_permissions(self, role_id):
        
        role_permissions = Role_Permission_M2M.objects.filter(role_id=role_id)
        permission_ids = [rp.permission_id for rp in role_permissions]
        permissions = Permissions.objects.filter(id__in=permission_ids)

        return permissions
    
    def create_new_role(self, role_data):
        roles = Roles.objects.create(**role_data) 
        # print(roles)
        return  roles

    def create_new_permission(self, perm_data):
        return Permissions.objects.create(**perm_data)
    
    def create_m2m_object(self, data):
        return Role_Permission_M2M.objects.create(**data)
    
    
    
    
