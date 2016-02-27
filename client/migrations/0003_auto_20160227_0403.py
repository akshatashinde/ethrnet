# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20160217_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='Address',
            field=models.ForeignKey(blank=True, to='account.UserAddress', null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='address_proof_types',
            field=models.CharField(default=b'Other', max_length=20, null=True, blank=True, choices=[(b'Aadhar', b'AADHAR'), (b'Driving Licence', b'DRIVING LICENCE'), (b'Electricity Bill', b'ELECTRICITY BILL'), (b'Other', b'OTHER'), (b'Passport', b'PASSPORT'), (b'Voter', b'VOTER')]),
        ),
        migrations.AlterField(
            model_name='client',
            name='id_proof_types',
            field=models.CharField(default=b'Other', max_length=20, null=True, blank=True, choices=[(b'Aadhar', b'AADHAR'), (b'Driving Licence', b'DRIVING LICENCE'), (b'Other', b'OTHER'), (b'PAN', b'PAN'), (b'Passport', b'PASSPORT'), (b'Voter', b'VOTER')]),
        ),
    ]
