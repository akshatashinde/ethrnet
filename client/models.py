from django.core.validators import RegexValidator
from django.db import models

from account.models import UserAddress
from user_auth.models import User


class Client(models.Model):
    name = models.CharField(max_length=250,)
    client_id = models.CharField(max_length=250)
    email = models.EmailField(max_length=255)
    Address = models.ForeignKey(UserAddress)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length="15")
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.client_id
