# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-12 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0006_stock_total_acumulado'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='ultimo_precio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
