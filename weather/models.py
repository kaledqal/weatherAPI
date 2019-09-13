from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManagaer(BaseUserManager):
    """Django uses this to manage users"""

    def create_user(self, email, password=None, **extra_fields):
        """
        The last bit says take any additional features with the user
        and use them .
        :param email:
        :param password:
        :param extra_fields:
        :return:
        """
        if not email:
            raise ValueError("Email Must Be Provided For new Users!")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """Create the super user"""
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """The user model for our project that supports using email  not username"""

    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManagaer()

    USERNAME_FIELD = 'email'