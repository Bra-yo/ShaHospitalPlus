# Generated by Django 5.1.6 on 2025-02-27 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalApp', '0002_doctors'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Doctors',
            new_name='Doctor',
        ),
    ]
