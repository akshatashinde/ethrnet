# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20160322_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='iteamvariation',
            name='model_no',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
