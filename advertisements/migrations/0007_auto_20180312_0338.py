# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0006_posts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='created_by',
        ),
        migrations.AddField(
            model_name='posts',
            name='created_by',
            field=models.ForeignKey(default=1, to='advertisements.Users'),
            preserve_default=False,
        ),
    ]
