# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='network',
            name='status',
            field=models.TextField(default='gray'),
            preserve_default=False,
        ),
    ]
