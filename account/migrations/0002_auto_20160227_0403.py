# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='city',
            field=models.CharField(default=b'Pune', max_length=120),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='state',
            field=models.CharField(default=b'Maharashtra', max_length=120, null=True, blank=True),
        ),
    ]
