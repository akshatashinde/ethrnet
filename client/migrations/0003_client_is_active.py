# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_client_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
