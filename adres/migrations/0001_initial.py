# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kullanici', '0002_auto_20170522_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adres_basligi', models.CharField(max_length=50)),
                ('adres', models.CharField(max_length=80)),
                ('sehir', models.CharField(max_length=40)),
                ('ilce', models.CharField(max_length=40)),
                ('mahalle', models.CharField(max_length=40)),
                ('sokak', models.CharField(max_length=40)),
                ('posta_kodu', models.CharField(max_length=40)),
                ('kullanici', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adres', to='kullanici.IsVeren')),
            ],
            options={
                'verbose_name_plural': 'İş Veren Adresleri',
                'verbose_name': 'İş Veren Adresi',
            },
        ),
    ]
