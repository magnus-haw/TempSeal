# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-11 06:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_remove_foodresponse_endtime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foodresponse',
            old_name='location',
            new_name='geom',
        ),
    ]