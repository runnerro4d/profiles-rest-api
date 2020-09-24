# to add to project make sure you add it with AUTH_USER_MODEL = 'profiles_api.UserProfile'
# at the bottom of the profiles_project/settings.py file

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for User Profiles"""

    def create_user(self,email,name,password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address') #makes sure a valid email is given

        email = self.normalize_email(email)
        user = self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db) #saves to default db

        return user

    def create_superuser(self,email,name,password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email,name,password) #automatically passes self

        user.is_superuser = True #automatically created by PermissionsMixin
        user.is_staff = True #specified below

        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for user in system"""
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Retrive full name of user """
        return self.name

    def get_short_name(self):
        """ Retrive short name of user """
        return self.name

    def __str__(self):
        """Return String Representation of our user"""
        return self.email
