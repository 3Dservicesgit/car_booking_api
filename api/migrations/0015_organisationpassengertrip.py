# Generated by Django 3.2.4 on 2021-09-27 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0014_organisationtrip'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganisationPassengerTrip',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('lastupdated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.UUIDField(default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'), primary_key=True, serialize=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_organisationpassengertrip_created', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('lastupdated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_organisationpassengertrip_lastmodified', to=settings.AUTH_USER_MODEL, verbose_name='Last modified by')),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.organisation')),
                ('passenger_trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.passengertrip')),
            ],
            options={
                'ordering': ['-lastupdated_at'],
                'abstract': False,
            },
        ),
    ]
