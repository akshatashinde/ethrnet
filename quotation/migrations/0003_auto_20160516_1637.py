# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0002_auto_20160516_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='created',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
