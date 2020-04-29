# Generated by Django 2.0.7 on 2020-04-29 10:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('maketime', '0002_auto_20200428_2303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('priority', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameField(
            model_name='event',
            old_name='description',
            new_name='notes',
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 4, 29, 10, 35, 39, 476221, tzinfo=utc)),
        ),
    ]
