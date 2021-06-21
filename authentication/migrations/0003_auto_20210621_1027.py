# Generated by Django 3.2.4 on 2021-06-21 10:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20210621_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='id',
            field=models.CharField(default=uuid.UUID('9f5d6b0f-d598-402d-8018-4c627ba0a3fd'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='fleetmanager',
            name='id',
            field=models.CharField(default=uuid.UUID('1dbb6d4f-3610-486e-b98b-41a1a83844fe'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='id',
            field=models.CharField(default=uuid.UUID('864a8930-a873-4c64-8d17-a20b62f614d1'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='systemadmin',
            name='id',
            field=models.CharField(default=uuid.UUID('cfb3e728-c339-4e11-bde3-4e4be06ab879'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='Id',
            field=models.CharField(default=uuid.UUID('b4564744-9bb6-4bd8-9cf5-8b225cca0524'), max_length=50, primary_key=True, serialize=False),
        ),
    ]