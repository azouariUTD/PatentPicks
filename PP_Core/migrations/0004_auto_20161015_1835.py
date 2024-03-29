# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PP_Core', '0003_auto_20161010_0517'),
    ]

    operations = [
        migrations.AddField(
            model_name='invention',
            name='picture',
            field=models.ImageField(default='static/PP_core/PP_Logo.png', upload_to='static/PP_core/'),
        ),
        migrations.AddField(
            model_name='inventiondetail',
            name='isPicked',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventiondetail',
            name='isViewed',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
