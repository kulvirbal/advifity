# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0004_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='user_type',
            new_name='usertype',
        ),
    ]
