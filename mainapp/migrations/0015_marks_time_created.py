# Generated by Django 3.0.6 on 2020-05-20 16:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_remove_marks_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='marks',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 20, 16, 11, 0, 386666, tzinfo=utc)),
        ),
    ]
