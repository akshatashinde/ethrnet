from django.db import models
from enum import Enum


class Enquiries(models.model):

    user_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    email = models.EmailField()
    plan = models.ForeignKey()
    address = models.TextField()
    landmark = models.CharField()
    created_on = models.DateTimeField(
        auto_now_add=True,
        null=False,
        editable=True,
    )
