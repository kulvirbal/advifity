# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0022_auto_20180320_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userpost',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('resume', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('cover_letter', models.TextField()),
                ('post', models.ForeignKey(to='advertisements.Posts')),
                ('user', models.ForeignKey(to='advertisements.Users')),
            ],
        ),
    ]
