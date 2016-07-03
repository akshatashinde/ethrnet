import datetime

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from account.models import Branch
from client.models import Client
from plans.models import Plans
from ethrnet.branch_manager import BranchWiseObjectManager


class Connection(models.Model):
    client = models.ForeignKey(Client)
    plan = models.ForeignKey(Plans)
    is_active = models.BooleanField(default=False)
    branch = models.ForeignKey(Branch, null=True, blank=True)
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
    expired_on = models.DateField()

    objects = BranchWiseObjectManager()

    def __unicode__(self):
        return self.branch.name + ' ' + self.client.name

    def save(self, *args, **kwargs):
        if self.pk is None:

            if self.plan:
                self.expired_on = datetime.datetime.now(
                ) + datetime.timedelta(days=self.plan.duration)
        else:
            pass
        super(Connection, self).save(*args, **kwargs)


class ConnectionHistory(models.Model):
    client = models.ForeignKey(Client)
    plan = models.ForeignKey(Plans)
    is_active = models.BooleanField(default=False)
    branch = models.ForeignKey(Branch, null=True, blank=True)
    created_on = models.DateTimeField(
        null=False,
        editable=True,
    )
    updated_on = models.DateTimeField(
        null=False,
        editable=True,
    )
    expired_on = models.DateField()

    objects = BranchWiseObjectManager()


@receiver(post_save, sender=Connection)
def connection_post_saved_receiver(sender, instance, created, *args, **kwargs):
    conn_hist = ConnectionHistory(client=instance.client)
    conn_hist.plan = instance.plan
    conn_hist.is_active = instance.is_active
    conn_hist.created_on = instance.created_on
    conn_hist.updated_on = instance.updated_on
    conn_hist.expired_on = instance.expired_on
    conn_hist.save()
