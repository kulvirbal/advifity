# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0017_remove_users_uploadedimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='uploadedImage',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
