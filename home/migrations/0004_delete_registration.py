# Generated by Django 4.2.2 on 2023-06-17 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_cnfmpass_registration_confirm'),
    ]

    operations = [
        migrations.DeleteModel(
            name='registration',
        ),
    ]