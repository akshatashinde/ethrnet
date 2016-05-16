from django.db import models
from account.models import UserAddress, Branch
from plans.models import Plans


class Enquiries(models.model):

    user_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    email = models.EmailField()
    plan = models.ForeignKey(Plans)
    address = models.ForeignKey(UserAddress)
    landmark = models.CharField()
    is_viewed = models.BooleanField(default=False)
    branch = models.ForeignKey(Branch)

    created_on = models.DateTimeField(
        auto_now_add=True,
        null=False,
        editable=True,
    )
