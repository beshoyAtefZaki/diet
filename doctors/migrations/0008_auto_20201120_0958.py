# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-11-20 09:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0007_auto_20201114_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mealstfr',
            name='patient',
        ),
        migrations.AlterField(
            model_name='doctorprofile',
            name='strat_date',
            field=models.DateField(default=datetime.datetime(2020, 11, 20, 9, 58, 7, 524812)),
        ),
    ]
