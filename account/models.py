from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
import os
from phonenumber_field.modelfields import PhoneNumberField

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calculatesite.settings')


class UserManager(BaseUserManager):

    def create_user(self, phone, email, password=None):
        
        if phone is None:
            raise TypeError('Users must have a phonenumber.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(phone=phone, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, phone, email, password):

        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(phone, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    phone = PhoneNumberField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','phone']

    objects = UserManager()

    def __str__(self):
        return self.email

    
    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    

