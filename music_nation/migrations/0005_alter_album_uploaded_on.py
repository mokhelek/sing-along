# Generated by Django 4.0.4 on 2022-08-28 22:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_nation', '0004_auto_20181004_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='uploaded_on',
            field=models.DateField(default=datetime.datetime(2022, 8, 28, 22, 20, 24, 357779)),
        ),
    ]
