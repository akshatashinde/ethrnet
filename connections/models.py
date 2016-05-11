from django.db import models

from account.models import Branch
from client.models import Client
from plans.models import Plans


class Connection(models.Model):
    client = models.ForeignKey(Client)
    plan = models.ForeignKey(Plans)
    is_active = models.BooleanField(default=False)
    branch = models.ForeignKey(Branch)
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
