# Generated by Django 3.0.6 on 2020-05-16 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20200516_0854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='user',
            new_name='u',
        ),
    ]
