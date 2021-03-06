# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-28 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_post_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tipologia',
            new_name='type',
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('Done', 'Done'), ('To-Do', 'To-Do')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='answer',
            field=models.TextField(default='', max_length=5020),
        ),
    ]
