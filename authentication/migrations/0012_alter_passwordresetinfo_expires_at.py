# Generated by Django 3.2.4 on 2021-09-15 07:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_auto_20210907_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetinfo',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 7, 32, 12, 616973, tzinfo=utc)),
        ),
    ]