# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ferienhausWeb', '0022_auto_20161226_2310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marker',
            name='icon',
        ),
        migrations.DeleteModel(
            name='markerIcon',
        ),
    ]
