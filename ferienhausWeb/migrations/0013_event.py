# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ferienhausWeb', '0012_auto_20161220_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('text', models.CharField(max_length=30)),
                ('details', models.CharField(max_length=50)),
            ],
        ),
    ]