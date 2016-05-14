# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 11:46
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_client_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex=b'^\\+?1?\\d{9,15}$')]),
        ),
    ]
