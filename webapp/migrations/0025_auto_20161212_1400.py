# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-12 14:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0024_auto_20161211_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date_invoice',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 12, 14, 0, 29, 100030, tzinfo=utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='invoiceline',
            name='product_id',
            field=models.ForeignKey(blank=True, default=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.Product'),
        ),
        migrations.AlterField(
            model_name='invoiceline',
            name='tax_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.Tax'),
        ),
    ]