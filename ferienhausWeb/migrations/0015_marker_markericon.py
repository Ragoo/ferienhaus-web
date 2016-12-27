# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ferienhausWeb.models
import location_field.models.plain
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ferienhausWeb', '0014_desc_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='marker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('info_text', ckeditor_uploader.fields.RichTextUploadingField()),
                ('coordinates', location_field.models.plain.PlainLocationField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='markerIcon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=ferienhausWeb.models.get_icon_path, default='')),
            ],
        ),
    ]
