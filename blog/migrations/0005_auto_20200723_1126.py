# Generated by Django 3.0.5 on 2020-07-23 05:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200723_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mlproject',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 23, 11, 26, 12, 887193)),
        ),
        migrations.AlterField(
            model_name='pythonproject',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 23, 11, 26, 12, 886192)),
        ),
        migrations.AlterField(
            model_name='webdevproject',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 23, 11, 26, 12, 887193)),
        ),
    ]
