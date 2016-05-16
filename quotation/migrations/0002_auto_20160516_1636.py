# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='created',
            field=models.DateTimeField(default=datetime.date(2016, 5, 16)),
        ),
    ]
