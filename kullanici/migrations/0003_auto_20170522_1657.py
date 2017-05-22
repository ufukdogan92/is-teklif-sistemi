# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 16:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kullanici', '0002_auto_20170522_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='isarayan',
            name='kullanici',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='is_arayan', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='isveren',
            name='kullanici',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='is_veren', to=settings.AUTH_USER_MODEL),
        ),
    ]
