from django.db import models
from django.conf import settings

from enum import Enum

from account.models import Branch


class Plans(models.Model):
    """
    Base Class capturing all plans information
    that provider can buy.
    """

    class PlanType(Enum):
        LIMITED = 'Limited'
        UNLIMITED = 'Unlimited'
        FUP = 'FUP'

        @classmethod
        def as_tuple(cls):
            return ((item.value, item.name.replace('_', ' ')) for item in cls)


    plan_type = models.CharField(blank=True, null=True, max_length=20,
                          choices=PlanType.as_tuple())
    price = models.FloatField(blank=True, null=True,)
    duration = models.IntegerField(blank=True, null=True,)
    download_speed = models.IntegerField(blank=True, null=True,)
    FUP_limit = models.IntegerField(blank=True, null=True,)
    post_FUP_speed = models.IntegerField(blank=True, null=True,)
    installation_charges = models.IntegerField(blank=True, null=True,)
    subscription_amount = models.IntegerField(blank=True, null=True,)
    branch = models.ForeignKey(Branch)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, related_name='plans_created_by')
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, related_name='plans_modified_by')
    is_active = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.plan_type) + ' '

    def get_price(self):
        return int(self.price)
