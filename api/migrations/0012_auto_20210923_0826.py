# Generated by Django 3.2.4 on 2021-09-23 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_driverrating_passengerrating_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blacklist',
            name='organisation',
        ),
        migrations.RemoveField(
            model_name='driverblacklist',
            name='reason',
        ),
        migrations.RemoveField(
            model_name='passengerblacklist',
            name='reason',
        ),
        migrations.RemoveField(
            model_name='vehicleblacklist',
            name='reason',
        ),
        migrations.AddField(
            model_name='blacklist',
            name='reason',
            field=models.CharField(default='not good', max_length=100),
        ),
    ]