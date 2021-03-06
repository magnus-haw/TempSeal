# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-07 22:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_remove_singleresponse_student_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='foodResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('student_ID', models.CharField(max_length=12)),
                ('room', models.PositiveIntegerField()),
                ('food', models.CharField(max_length=50)),
                ('endTime', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='building',
            name='coldvotes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='building',
            name='coolvotes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='building',
            name='hotvotes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='building',
            name='okvotes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='building',
            name='warmvotes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='foodresponse',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Building'),
        ),
    ]
