# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ferienhausWeb.models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ferienhausWeb', '0023_auto_20161226_2319'),
    ]

    operations = [
        migrations.CreateModel(
            name='markerIcon',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=ferienhausWeb.models.get_icon_path, default='')),
            ],
        ),
        migrations.AddField(
            model_name='marker',
            name='icon',
            field=models.ForeignKey(to='ferienhausWeb.markerIcon', default=1, on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
