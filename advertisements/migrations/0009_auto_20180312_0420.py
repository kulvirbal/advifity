# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0008_auto_20180312_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
