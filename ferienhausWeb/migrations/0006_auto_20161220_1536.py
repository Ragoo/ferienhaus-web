# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 14:36
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ferienhausWeb', '0005_auto_20161220_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='picture',
        ),
        migrations.AlterField(
            model_name='guestbook',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
