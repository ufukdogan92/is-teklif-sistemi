# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 16:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teklif', '0003_auto_20170522_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='Odeme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('odeme_basligi', models.CharField(blank=True, max_length=40, null=True)),
                ('ucret', models.IntegerField(blank=True, null=True)),
                ('odemeTuru', models.CharField(choices=[('H', 'Havale'), ('N', 'Nakit'), ('O', 'Online Ödeme')], default='N', max_length=3)),
                ('tamamlanma_durumu', models.BooleanField(default=False)),
                ('teklif', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='odeme_teklifi', to='teklif.Teklif')),
            ],
            options={
                'verbose_name_plural': 'Ödemeler',
                'verbose_name': 'Ödeme',
            },
        ),
    ]
