# Generated by Django 4.1 on 2022-08-29 19:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_nation', '0008_alter_album_uploaded_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='image',
        ),
        migrations.AlterField(
            model_name='album',
            name='uploaded_on',
            field=models.DateField(default=datetime.datetime(2022, 8, 29, 19, 36, 26, 467962, tzinfo=datetime.timezone.utc)),
        ),
    ]