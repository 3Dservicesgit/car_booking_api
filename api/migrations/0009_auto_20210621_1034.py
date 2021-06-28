# Generated by Django 3.2.4 on 2021-06-21 10:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210621_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blacklist',
            name='id',
            field=models.CharField(default=uuid.UUID('0844a3f7-3153-4e33-ba4b-545ceda98280'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='branch',
            name='id',
            field=models.CharField(default=uuid.UUID('b9c7475d-e7f5-4fbf-8689-40d26d817765'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.CharField(default=uuid.UUID('21fcc03c-db18-4d71-8cb9-1441de676936'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='directorate',
            name='id',
            field=models.CharField(default=uuid.UUID('e3d72e56-878a-46cb-a1a9-b33006e45ab1'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='directoratedepartment',
            name='id',
            field=models.CharField(default=uuid.UUID('97bced51-dce9-4eec-b74d-3857d9d7b822'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='driverblacklist',
            name='id',
            field=models.CharField(default=uuid.UUID('ef50b414-b5ae-46e2-afa7-372b69474a75'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='drivertrip',
            name='id',
            field=models.CharField(default=uuid.UUID('1ed6c987-e904-498a-83e2-bbc0c0b8939a'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='fleetmanagertrip',
            name='id',
            field=models.CharField(default=uuid.UUID('a60ffec5-7cda-40ad-8c30-ea4c30d195ac'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='id',
            field=models.CharField(default=uuid.UUID('1e5cb0eb-c978-4478-89a4-794f4c3af21b'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='organisationdriver',
            name='id',
            field=models.CharField(default=uuid.UUID('a1e66e14-d109-40a7-bb27-791c269d0d94'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='organisationfleetmanager',
            name='id',
            field=models.CharField(default=uuid.UUID('06015801-767a-4eb0-9ee4-ecb368b8432d'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='organisationvehicle',
            name='id',
            field=models.CharField(default=uuid.UUID('ddd4c809-d8e9-40bd-bfa3-b7dcae910d90'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='passengerblacklist',
            name='id',
            field=models.CharField(default=uuid.UUID('6a18ffee-b1e3-4e04-8c4d-f526a2fbec60'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='passengertrip',
            name='id',
            field=models.CharField(default=uuid.UUID('26fe7337-806b-43b3-9e10-35146dfecb97'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.CharField(default=uuid.UUID('19e4e7f0-a9eb-4399-868c-51587cf33c8a'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='projectvehicledeploy',
            name='id',
            field=models.CharField(default=uuid.UUID('648604da-6369-4838-aece-940fbd3f65b6'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='region',
            name='id',
            field=models.CharField(default=uuid.UUID('5a361fc9-469d-424f-8150-f95204179f26'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='station',
            name='id',
            field=models.CharField(default=uuid.UUID('3139aebe-fcc5-4c57-90ce-78ce12f3cac0'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stationvehicledeploy',
            name='id',
            field=models.CharField(default=uuid.UUID('91b44fd2-15ba-4bec-894f-4a452135d560'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='trip',
            name='id',
            field=models.CharField(default=uuid.UUID('6f638dc0-54a9-4c19-b59f-5ac454aaa561'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='id',
            field=models.CharField(default=uuid.UUID('2ec3d433-54f6-4ff7-8ac4-591b33c5072c'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vehicleblacklist',
            name='id',
            field=models.CharField(default=uuid.UUID('c5697086-b4fe-48fe-9c03-2a99aa40c944'), max_length=50, primary_key=True, serialize=False),
        ),
    ]