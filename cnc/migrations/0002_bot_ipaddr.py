# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-29 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cnc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='ipaddr',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]