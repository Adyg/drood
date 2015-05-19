# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import user_profile.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OPMLStorage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('opml_file', models.FileField(upload_to=user_profile.models.opml_directory)),
                ('import_status', models.CharField(default=b'P', max_length=1, choices=[(b'P', b'Pending'), (b'I', b'Imported'), (b'F', b'Failed')])),
            ],
        ),
    ]
