# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherForecast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('city', models.IntegerField()),
                ('min_temp', models.FloatField()),
                ('max_temp', models.FloatField()),
                ('wind', models.FloatField()),
                ('rain', models.FloatField()),
                ('meta', models.TextField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='weatherforecast',
            unique_together=set([('date', 'city')]),
        ),
    ]
