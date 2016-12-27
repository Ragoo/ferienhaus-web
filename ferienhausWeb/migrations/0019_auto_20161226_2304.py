# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ferienhausWeb', '0018_auto_20161226_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='markericon',
            name='id',
        ),
        migrations.AlterField(
            model_name='marker',
            name='icon',
            field=models.ForeignKey(to='ferienhausWeb.markerIcon', default=1, on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterField(
            model_name='markericon',
            name='name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
