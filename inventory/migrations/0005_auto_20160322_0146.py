# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_iteamvariation_model_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventoryitem',
            name='quantity',
        ),
        migrations.AddField(
            model_name='iteamvariation',
            name='quantity',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
