# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0011_auto_20180312_0531'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='hourly_rate',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posts',
            name='job_type',
            field=models.ForeignKey(default=1, to='advertisements.Types'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posts',
            name='organization',
            field=models.CharField(default=datetime.datetime(2018, 3, 13, 0, 39, 7, 738914, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
    ]
