# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 16:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teklif', '0005_teklifonay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teklifonay',
            name='teklif',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teklif_onay', to='teklif.Teklif'),
        ),
    ]
