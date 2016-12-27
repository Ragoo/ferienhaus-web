# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('ferienhausWeb', '0015_marker_markericon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='coordinates',
            field=location_field.models.plain.PlainLocationField(default='53.653734673045015,7.784392833709716', max_length=63),
        ),
    ]
