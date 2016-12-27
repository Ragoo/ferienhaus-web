# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ferienhausWeb', '0021_markericon_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='markericon',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False),
        ),
        migrations.AlterField(
            model_name='markericon',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
