# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0016_auto_20180319_0243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='uploadedImage',
        ),
    ]
