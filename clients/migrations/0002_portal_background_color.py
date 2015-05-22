# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portal',
            name='background_color',
            field=models.CharField(max_length=7, null=True),
            preserve_default=True,
        ),
    ]
