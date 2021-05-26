# Generated by Django 3.2.3 on 2021-05-26 14:21

import django.contrib.auth.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20210526_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='id',
            field=models.CharField(default=uuid.UUID('4d204f5e-b773-49b9-bdd7-970938074a90'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='fleetmanager',
            name='id',
            field=models.CharField(default=uuid.UUID('a7b58c7f-4ee1-4320-aa5c-ecec540f0a87'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='id',
            field=models.CharField(default=uuid.UUID('d784bcc9-7b48-427d-8a41-0eb7805a1b67'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='systemadmin',
            name='id',
            field=models.CharField(default=uuid.UUID('0b4e66be-045b-4635-b713-10d639b3503b'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='Id',
            field=models.CharField(default=uuid.UUID('25b15415-19a7-42df-ab80-2bd970c2f805'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
