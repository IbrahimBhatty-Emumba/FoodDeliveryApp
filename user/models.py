from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# class Users(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)
#     password = models.CharField(max_length=300)
#     type = models.CharField(max_length=50)
#     address = models.CharField(max_length=300)
#     phone = models.CharField(max_length=200)
#     created_date = models.DateField(auto_now_add=True)

#     class Meta:
#         managed = True
#         db_table = 'users'

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


class Users(AbstractUser):
    username = None
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=50)
    class Meta:
        managed = True
        db_table = 'users'
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return str(self.id)


