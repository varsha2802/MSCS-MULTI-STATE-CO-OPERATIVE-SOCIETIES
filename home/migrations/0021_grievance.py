# Generated by Django 4.2.2 on 2023-06-22 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_delete_grievance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grievance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('typeofcomplaint', models.CharField(max_length=30)),
                ('societycomplaint', models.CharField(max_length=150)),
                ('complaint', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]