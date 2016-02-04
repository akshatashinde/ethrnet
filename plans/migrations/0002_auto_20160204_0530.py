# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plans',
            name='created_by',
            field=models.ForeignKey(related_name='plans_created_by', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='plans',
            name='updated_by',
            field=models.ForeignKey(related_name='plans_modified_by', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
