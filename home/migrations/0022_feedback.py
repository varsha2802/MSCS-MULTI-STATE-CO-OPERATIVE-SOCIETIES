# Generated by Django 4.2.2 on 2023-06-22 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_grievance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeoffeedback', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
                ('address', models.TextField()),
                ('subject', models.TextField()),
                ('file', models.FileField(upload_to='feedback/')),
                ('date', models.DateField()),
            ],
        ),
    ]