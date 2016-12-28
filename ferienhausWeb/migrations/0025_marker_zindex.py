# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ferienhausWeb', '0024_auto_20161226_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='zIndex',
            field=models.IntegerField(max_length=3, default=1),
        ),
    ]
