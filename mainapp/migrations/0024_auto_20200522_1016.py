# Generated by Django 3.0.6 on 2020-05-22 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0023_auto_20200522_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='marks',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='people',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
