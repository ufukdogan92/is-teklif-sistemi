# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-23 06:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hizmet', '0002_auto_20170522_1310'),
        ('ilan', '0009_auto_20170523_0645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ilan',
            name='hizmet',
        ),
        migrations.AddField(
            model_name='ilan',
            name='hizmet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='hizmet_kategorisi', to='hizmet.HizmetDescription'),
            preserve_default=False,
        ),
    ]
