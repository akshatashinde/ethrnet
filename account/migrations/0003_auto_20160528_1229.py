# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20160329_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='country',
            field=models.CharField(default=b'India', max_length=120, null=True, blank=True),
        ),
    ]
