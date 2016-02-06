from django.db import models
from account.models import UserAddress
from plans.models import Plans


class Enquiries(models.model):

    user_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    email = models.EmailField()
    plan = models.ForeignKey(Plans)
    address = models.ForeignKey(UserAddress)
    landmark = models.CharField()
    is_viewed = models.BooleanField(default=False)
    created_on = models.DateTimeField(
        auto_now_add=True,
        null=False,
        editable=True,
    )
