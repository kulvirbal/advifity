# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0025_auto_20180403_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='created_by',
        ),
    ]
