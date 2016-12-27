# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ferienhausWeb', '0020_auto_20161226_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='markericon',
            name='id',
            field=models.IntegerField(default=1),
        ),
    ]
