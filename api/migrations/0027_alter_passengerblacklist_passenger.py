# Generated by Django 3.2.4 on 2021-10-25 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0035_alter_passwordresetinfo_expires_at'),
        ('api', '0026_alter_departmentdriver_driver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passengerblacklist',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.passenger'),
        ),
    ]
