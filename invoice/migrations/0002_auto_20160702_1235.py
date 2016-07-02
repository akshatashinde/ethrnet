# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('client', '0001_initial'),
        ('plans', '0001_initial'),
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceitem',
            name='plan',
            field=models.ForeignKey(blank=True, to='plans.Plans', null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='address',
            field=models.ForeignKey(related_name='invoice_set', to='account.UserAddress'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='branch',
            field=models.ForeignKey(blank=True, to='account.Branch', null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='currency',
            field=models.ForeignKey(blank=True, to='invoice.Currency', null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='user',
            field=models.ForeignKey(to='client.Client'),
        ),
    ]
