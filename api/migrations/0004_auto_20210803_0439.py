# Generated by Django 3.2.4 on 2021-08-03 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_trip_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='ended_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='started_at',
            field=models.DateTimeField(null=True),
        ),
    ]