from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):

    use_in_migration = False

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)

class Permissions(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=100, default="NO_NAME")
    endpoint = models.CharField(max_length=100)

class Roles(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=100)

class Role_Permission_M2M(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permissions, on_delete=models.CASCADE)

class Users(AbstractUser):
    username = None
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE, default=1)
    class Meta:
        managed = True
        db_table = 'users'
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return str(self.id)




