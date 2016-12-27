# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ferienhausWeb', '0019_auto_20161226_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='icon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ferienhausWeb.markerIcon', default=1),
        ),
    ]
