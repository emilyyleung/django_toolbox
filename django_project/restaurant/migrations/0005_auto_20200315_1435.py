# Generated by Django 2.0.7 on 2020-03-15 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_auto_20200315_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='dish_course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='restaurant.Course'),
        ),
    ]
