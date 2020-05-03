# Generated by Django 2.0.7 on 2020-05-03 22:20

import datetime
import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('maketime', '0025_auto_20200503_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurrence',
            name='bysetpos',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message=None)]),
        ),
        migrations.AlterField(
            model_name='recurrence',
            name='until',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 31, 23, 59, 59, 414374)),
        ),
    ]
