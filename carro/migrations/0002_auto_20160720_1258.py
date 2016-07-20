# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-20 12:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carro', '0001_initial'),
        ('pedido', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='pedido',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pedido.Pedido'),
        ),
        migrations.AddField(
            model_name='carro',
            name='propietario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Carrito', to=settings.AUTH_USER_MODEL),
        ),
    ]