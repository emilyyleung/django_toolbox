# Generated by Django 2.0.7 on 2020-05-07 20:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maketime', '0030_auto_20200505_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurrence',
            name='until',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 31, 23, 59, 59, 66802)),
        ),
    ]
