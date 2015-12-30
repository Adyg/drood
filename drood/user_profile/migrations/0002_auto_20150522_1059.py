# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opmlstorage',
            name='import_status',
            field=models.CharField(default=b'P', max_length=1, choices=[(b'P', b'Pending'), (b'I', b'Imported'), (b'F', b'Failed'), (b'R', b'Import running')]),
        ),
    ]
