# Generated by Django 3.1.1 on 2020-10-26 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_photo_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
