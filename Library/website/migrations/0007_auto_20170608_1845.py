# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20170608_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuebook',
            name='noOfDays',
            field=models.CharField(default=0, max_length=3),
        ),
    ]