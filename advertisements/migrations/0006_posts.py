# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0005_auto_20180311_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('address', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ManyToManyField(to='advertisements.Users')),
            ],
        ),
    ]
