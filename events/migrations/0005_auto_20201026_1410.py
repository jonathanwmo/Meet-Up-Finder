# Generated by Django 3.1.1 on 2020-10-26 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20201026_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='photo',
            field=models.ImageField(null=True, upload_to='events/static/events/images/<property object at 0x7fde11502230>'),
        ),
    ]
