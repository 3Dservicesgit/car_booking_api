# Generated by Django 3.2.4 on 2021-10-25 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_alter_passengerblacklist_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmentdriver',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.organisationdriver'),
        ),
    ]
