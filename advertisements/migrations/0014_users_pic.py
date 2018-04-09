# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0013_users_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='pic',
            field=models.CharField(default='default.png', max_length=255),
            preserve_default=False,
        ),
    ]
