from django.db import models
from django.contrib.auth.models import User

from enum import Enum


class Plans(models.Model):
    """
    Base Class capturing all plans information
    that provider can buy.
    """

    class PlanType(Enum):
        COMMERTIAL = 'Commertial'
        PERSONAL = 'Personal'


    plan_type = models.CharField(null=True, max_length=20,
                          choices=PlanType.as_tuple())
    price = models.FloatField()
    duration = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='plans_created_by')
    updated_by = models.ForeignKey(
        User, blank=True, null=True, related_name='plans_modified_by')
    is_active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.plan_type
