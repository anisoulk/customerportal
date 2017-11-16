# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_network_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='network',
            name='ip_ping',
            field=models.TextField(default='192.168.201.37'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='network',
            name='ip_switch',
            field=models.TextField(default='192.168.201.37'),
            preserve_default=False,
        ),
    ]