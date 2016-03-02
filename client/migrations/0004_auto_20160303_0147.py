# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '__first__'),
        ('client', '0003_auto_20160227_0403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='attachments',
        ),
        migrations.AddField(
            model_name='client',
            name='attachments',
            field=models.ManyToManyField(to='fileupload.Picture', null=True, blank=True),
        ),
    ]
