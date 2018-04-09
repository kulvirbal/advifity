# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0024_messages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messages',
            old_name='address',
            new_name='message',
        ),
    ]
