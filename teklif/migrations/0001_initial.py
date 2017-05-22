# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 15:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kullanici', '0002_auto_20170522_1427'),
        ('ilan', '0005_auto_20170522_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teklif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('butce', models.IntegerField()),
                ('sure', models.IntegerField()),
                ('tamamlanma_durumu', models.BooleanField(default=False)),
                ('teklif_tarihi', models.DateTimeField(auto_now_add=True)),
                ('duzenlenme_tarihi', models.DateField(auto_now=True)),
                ('ilan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='odeme_ilanı', to='ilan.Ilan')),
                ('kullanici', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_arayan', to='kullanici.IsArayan')),
            ],
            options={
                'verbose_name': 'Teklifler',
                'verbose_name_plural': 'Teklif',
            },
        ),
    ]
