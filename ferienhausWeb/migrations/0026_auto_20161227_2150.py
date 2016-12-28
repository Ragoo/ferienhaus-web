# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('ferienhausWeb', '0025_marker_zindex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='zIndex',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(1)], default=1),
        ),
    ]
