# Generated by Django 3.2.4 on 2021-10-14 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_fleetmanagernotification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='expo_token',
            field=models.CharField(max_length=255),
        ),
    ]
