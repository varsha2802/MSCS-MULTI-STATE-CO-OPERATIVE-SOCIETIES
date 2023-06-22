# Generated by Django 4.2.2 on 2023-06-20 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_delete_graphdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraphData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('graph_data', models.TextField()),
                ('graph_img', models.ImageField(upload_to=None)),
            ],
        ),
    ]
