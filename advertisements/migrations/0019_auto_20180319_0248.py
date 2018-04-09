# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0018_users_uploadedimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='address',
        ),
        migrations.RemoveField(
            model_name='users',
            name='uploadedImage',
        ),
    ]
