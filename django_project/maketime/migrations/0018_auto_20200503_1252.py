# Generated by Django 2.0.7 on 2020-05-03 02:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('maketime', '0017_auto_20200503_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurrence',
            name='tzid',
            field=models.CharField(default=datetime.datetime(2020, 5, 3, 2, 52, 54, 272523, tzinfo=utc), max_length=200),
        ),
        migrations.AlterField(
            model_name='recurrence',
            name='until',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 31, 23, 59, 59, 272523)),
        ),
    ]