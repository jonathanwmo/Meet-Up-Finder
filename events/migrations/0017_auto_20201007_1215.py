# Generated by Django 3.1.1 on 2020-10-07 16:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_auto_20201005_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 7, 16, 15, 2, 876837, tzinfo=utc)),
        ),
    ]
