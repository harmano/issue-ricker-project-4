# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-24 01:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.RemoveField(
            model_name='post',
            name='price',
        ),
    ]
