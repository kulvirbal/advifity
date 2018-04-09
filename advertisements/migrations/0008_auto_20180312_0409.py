# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0007_auto_20180312_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
