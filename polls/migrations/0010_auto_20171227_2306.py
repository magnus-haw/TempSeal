# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-28 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20171215_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='singleresponse',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='singleresponse',
            name='email',
            field=models.EmailField(default='mhaw@caltech.edu', max_length=254),
            preserve_default=False,
        ),
    ]
