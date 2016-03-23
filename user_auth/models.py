from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from enum import Enum


class UserManager(BaseUserManager):
    """
    Creating UserManager class from BaseUserManager
    (overridding create_user and create_superuser)
    so that users can be created using email instead of
    user_name.
    """

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The given email address must be set')

        now = timezone.now()
        email = UserManager.normalize_email(email)
        user = self.model(email=email,
                          is_staff=False, is_active=True, is_superuser=False,
                          last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        superuser = self.create_user(email, password, **extra_fields)
        superuser.is_staff = True
        superuser.is_active = True
        superuser.is_superuser = True
        superuser.is_email_verified = True
        superuser.save(using=self._db)
        return superuser


class User(AbstractBaseUser, PermissionsMixin):
    """
    Creating custom user models using AbstractBaseUser.
    Adding custom fields (phone number) to the base user model.
    Implementing Validation on phone number.
    """

    class UserTypes(Enum):
        ADMIN = 'Admin'
        NORMAL_USER = 'Normal User'

        @classmethod
        def as_tuple(cls):
            return ((item.value, item.name.replace('_', ' ')) for item in cls)

    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=80, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    username = models.CharField(max_length=50, blank=True, null=True)
    date_joined = models.DateTimeField(
        auto_now_add=True,
        null=False,
        editable=True,
    )
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format:' \
        ' '+999999999'. Up to 15 digits allowed.")

    phone_number = models.CharField(validators=[phone_regex], max_length=15,
                                    null=True, blank=True)

    role = models.CharField(
        null=True, max_length=50,
        choices=UserTypes.as_tuple(),
        default=UserTypes.NORMAL_USER.value
    )

    USERNAME_FIELD = 'email'

    objects = UserManager()

    # Returns full name of user
    def get_full_name(self):
        return self.full_name

    # Returns short name of user.
    def get_short_name(self):
        return self.full_name


@receiver(post_save, sender=User)
def create_username(sender, instance=None,
                    created=False, **kwargs):
    """
    When a new user is created this fuctions creates a
    asociated username for newly created user
    """
    if created:
        if instance.phone_number:
            instance.username = instance.phone_number + instance.email
        else:
            instance.username = instance.email
        instance.save()
