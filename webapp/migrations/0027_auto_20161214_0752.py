# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-14 07:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0026_auto_20161213_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date_invoice',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 14, 7, 52, 51, 37735, tzinfo=utc), verbose_name='Date'),
        ),
    ]