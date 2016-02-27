from django.core.validators import RegexValidator
from django.db import models
from enum import Enum
from account.models import UserAddress
from user_auth.models import User
from fileupload.models import Picture


class Client(models.Model):
    class Gender(Enum):
        MALE = 'Male'
        FEMALE = 'Female'
        OTHER = 'Other'

        @classmethod
        def as_tuple(cls):
            return ((item.value, item.name.replace('_', ' ')) for item in cls)

    class Id_proofs(Enum):
        PASSPORT = 'Passport'
        DRIVING_LICENCE = 'Driving Licence'
        PAN = 'PAN'
        AADHAR = 'Aadhar'
        VOTER = 'Voter'
        OTHER = 'Other'

        @classmethod
        def as_tuple(cls):
            return ((item.value, item.name.replace('_', ' ')) for item in cls)

    class Address_proofs(Enum):
        PASSPORT = 'Passport'
        DRIVING_LICENCE = 'Driving Licence'
        ELECTRICITY_BILL = 'Electricity Bill'
        AADHAR = 'Aadhar'
        VOTER = 'Voter'
        OTHER = 'Other'

        @classmethod
        def as_tuple(cls):
            return ((item.value, item.name.replace('_', ' ')) for item in cls)

    name = models.CharField(max_length=250)
    client_id = models.CharField(max_length=250)
    email = models.EmailField(max_length=255)
    Address = models.ForeignKey(UserAddress, null=True, blank=True)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length="15")

    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(null=True, max_length=20, default='Other',
                              choices=Gender.as_tuple())

    id_proof_types = models.CharField(null=True, blank=True, max_length=20, default='Other',
                                      choices=Id_proofs.as_tuple())
    address_proof_types = models.CharField(null=True, blank=True, max_length=20,  default='Other',
                                           choices=Address_proofs.as_tuple())

    attachments = models.ForeignKey(Picture, null=True, blank=True)

    created_by = models.ForeignKey(User)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.client_id
