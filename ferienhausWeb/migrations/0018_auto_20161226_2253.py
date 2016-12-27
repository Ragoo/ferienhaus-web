# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ferienhausWeb', '0017_marker_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='icon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ferienhausWeb.markerIcon', blank=True, null=True),
        ),
    ]
