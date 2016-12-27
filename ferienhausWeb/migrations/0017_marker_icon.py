# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ferienhausWeb', '0016_auto_20161226_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='icon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=1, to='ferienhausWeb.markerIcon'),
        ),
    ]
