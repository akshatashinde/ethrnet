# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('client', '0001_initial'),
        ('plans', '0001_initial'),
        ('connections', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='connectionhistory',
            name='plan',
            field=models.ForeignKey(to='plans.Plans'),
        ),
        migrations.AddField(
            model_name='connection',
            name='branch',
            field=models.ForeignKey(blank=True, to='account.Branch', null=True),
        ),
        migrations.AddField(
            model_name='connection',
            name='client',
            field=models.ForeignKey(to='client.Client'),
        ),
        migrations.AddField(
            model_name='connection',
            name='plan',
            field=models.ForeignKey(to='plans.Plans'),
        ),
    ]
