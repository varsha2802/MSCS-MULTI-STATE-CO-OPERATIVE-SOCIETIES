# Generated by Django 4.2.2 on 2023-06-20 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_graphdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphdata',
            name='graph_img',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
