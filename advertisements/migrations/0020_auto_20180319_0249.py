# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0019_auto_20180319_0248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='job_type',
        ),
        migrations.DeleteModel(
            name='Posts',
        ),
        migrations.DeleteModel(
            name='Types',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
