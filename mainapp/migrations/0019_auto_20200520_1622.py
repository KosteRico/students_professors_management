# Generated by Django 3.0.6 on 2020-05-20 16:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_auto_20200520_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 20, 16, 22, 4, 664267, tzinfo=utc)),
        ),
    ]
