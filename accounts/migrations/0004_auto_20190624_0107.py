# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-24 01:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190621_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.DecimalField(decimal_places=2, default='', max_digits=6),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
