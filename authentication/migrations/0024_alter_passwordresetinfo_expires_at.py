# Generated by Django 3.2.4 on 2021-10-14 06:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0023_alter_passwordresetinfo_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetinfo',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 15, 6, 17, 48, 870556, tzinfo=utc)),
        ),
    ]