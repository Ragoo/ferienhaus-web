# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 17:12
from __future__ import unicode_literals

from django.db import migrations, models
import ferienhausWeb.models


class Migration(migrations.Migration):

    dependencies = [
        ('ferienhausWeb', '0009_auto_20161220_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeryimage',
            name='image',
            field=models.FileField(blank=True, default='', null=True, upload_to=ferienhausWeb.models.get_image_path),
        ),
    ]
