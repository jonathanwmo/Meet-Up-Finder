# Generated by Django 3.1.1 on 2020-10-28 15:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0011_event_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='invitees',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]