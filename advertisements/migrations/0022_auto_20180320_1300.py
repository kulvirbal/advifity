# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0021_auto_20180319_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='users',
            name='usertype',
            field=models.IntegerField(default=1),
        ),
    ]
