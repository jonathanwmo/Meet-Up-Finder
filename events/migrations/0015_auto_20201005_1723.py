# Generated by Django 3.1.1 on 2020-10-05 21:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_auto_20201005_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventtag',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 5, 21, 23, 57, 587166, tzinfo=utc)),
        ),
    ]
