# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0002_auto_20180306_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='types',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
