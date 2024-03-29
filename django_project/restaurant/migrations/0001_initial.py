# Generated by Django 2.0.7 on 2020-03-15 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=200)),
                ('translation', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(default='')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=99999)),
                ('vegan', models.BooleanField(default=False)),
                ('vegetarian_option', models.BooleanField(default=False)),
                ('gluten_free', models.BooleanField(default=False)),
                ('signature_dish', models.BooleanField(default=False)),
                ('spice_level', models.IntegerField(default=0)),
                ('pieces', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Dishes',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('dishes', models.ManyToManyField(to='restaurant.Dish')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(to='restaurant.Order'),
        ),
    ]
