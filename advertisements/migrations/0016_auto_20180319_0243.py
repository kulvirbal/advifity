# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0015_auto_20180319_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='uploadedImage',
            field=models.ImageField(upload_to=b'static/%m/%d'),
        ),
    ]
