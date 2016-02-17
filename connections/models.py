from django.db import models
from client.models import Client
from plans.models import Plans


class Connection(models.Model):
    client = models.ForeignKey(Client)
    plan = models.ForeignKey(Plans)
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
