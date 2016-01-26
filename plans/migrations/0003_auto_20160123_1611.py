# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0002_auto_20160123_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plans',
            name='FUP_limit',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='plans',
            name='created_by',
            field=models.ForeignKey(related_name='plans_created_by', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='plans',
            name='download_speed',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='plans',
            name='duration',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='plans',
            name='installation_charges',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='plans',
            name='plan_type',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[(b'Commertial', b'COMMERTIAL'), (b'Personal', b'PERSONAL')]),
        ),
        migrations.AlterField(
            model_name='plans',
            name='post_FUP_speed',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='plans',
            name='price',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='plans',
            name='subscription_amount',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
