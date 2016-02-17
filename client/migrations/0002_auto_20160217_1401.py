# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '__first__'),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='address_proof_types',
            field=models.CharField(default=b'Other', max_length=20, null=True, choices=[(b'Aadhar', b'AADHAR'), (b'Driving Licence', b'DRIVING LICENCE'), (b'Electricity Bill', b'ELECTRICITY BILL'), (b'Other', b'OTHER'), (b'Passport', b'PASSPORT'), (b'Voter', b'VOTER')]),
        ),
        migrations.AddField(
            model_name='client',
            name='attachments',
            field=models.ForeignKey(blank=True, to='fileupload.Picture', null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='birth_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='client',
            name='gender',
            field=models.CharField(default=b'Other', max_length=20, null=True, choices=[(b'Female', b'FEMALE'), (b'Male', b'MALE'), (b'Other', b'OTHER')]),
        ),
        migrations.AddField(
            model_name='client',
            name='id_proof_types',
            field=models.CharField(default=b'Other', max_length=20, null=True, choices=[(b'Aadhar', b'AADHAR'), (b'Driving Licence', b'DRIVING LICENCE'), (b'Other', b'OTHER'), (b'PAN', b'PAN'), (b'Passport', b'PASSPORT'), (b'Voter', b'VOTER')]),
        ),
    ]
