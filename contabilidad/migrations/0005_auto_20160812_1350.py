# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-12 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0004_auto_20160807_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='operacion_stock',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contabilidad.Stock'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='num_operacion',
            field=models.CharField(blank=True, editable=False, max_length=100),
        ),
    ]