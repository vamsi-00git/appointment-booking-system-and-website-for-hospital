# Generated by Django 5.1.4 on 2024-12-17 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_alter_appointment_doctor_alter_doctor_specialization'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
