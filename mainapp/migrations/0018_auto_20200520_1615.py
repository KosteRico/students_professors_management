# Generated by Django 3.0.6 on 2020-05-20 16:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_auto_20200520_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 20, 16, 15, 26, 940493, tzinfo=utc)),
        ),
    ]
