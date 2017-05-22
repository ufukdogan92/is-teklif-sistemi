# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ilan', '0005_auto_20170522_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='ilan',
            name='sureUzunlugu',
            field=models.CharField(choices=[('TL', 'Türk Lirası'), ('DLR', 'DOLAR'), ('EUR', 'EURO')], default='TL', max_length=3),
        ),
        migrations.AlterField(
            model_name='ilan',
            name='butceTipi',
            field=models.CharField(choices=[('S', 'Saat'), ('G', 'Gün'), ('A', 'Ay'), ('H', 'Hafta'), ('Y', 'Yıl')], default='G', max_length=3),
        ),
    ]