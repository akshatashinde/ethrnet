from django.db import models
from enum import Enum


class Connection(models.model):

    class Gender(Enum):
        MALE = 'Male'
        FEMALE = 'Female'
        OTHERS = 'Others'

    class Id_proofs(Enum):
        PASSPORT = 'Passport'
        DRIVING_LICENCE = 'Driving Licence'
        PAN = 'PAN'
        AADHAR = 'Aadhar'
        VOTER = 'Voter'

    class Address_proofs(Enum):
        PASSPORT = 'Passport'
        DRIVING_LICENCE = 'Driving Licence'
        ELECTRICITY_BILL = 'Electricity Bill'
        AADHAR = 'Aadhar'
        VOTER = 'Voter'

    user_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    email = models.EmailField()
    plan = models.ForeignKey()
    address = models.TextField()
    landmark = models.CharField()
    birth_date = models.DateTimeField()
    gender = models.CharField(null=True, max_length=20,
                              choices=Gender.as_tuple())

    id_proof_types = models.CharField(null=True, max_length=20,
                          choices=Id_proofs.as_tuple())
    id_proof = models.ImageField()

    address_proof_types = models.CharField(null=True, max_length=20,
                          choices=Address_proofs.as_tuple())
    address_proof = models.ImageField()

    is_active = models.BooleanField(default=False)
    created_on = models.DateTimeField(
        auto_now_add=True,
        null=False,
        editable=True,
    )
    updated_on = models.DateTimeField(
        auto_now_add=True,
        null=False,
        editable=True,
    )
    expired_on = models.DateTimeField()
