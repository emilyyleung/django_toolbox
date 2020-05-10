# Generated by Django 2.0.7 on 2020-05-05 22:42

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maketime', '0027_auto_20200503_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurrence',
            name='testbysetpos',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator(regex='^[A-Z]:[A-Z]$')]),
        ),
        migrations.AlterField(
            model_name='recurrence',
            name='until',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 31, 23, 59, 59, 349489)),
        ),
    ]