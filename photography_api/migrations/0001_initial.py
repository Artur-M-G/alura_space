# Generated by Django 5.0.2 on 2024-02-26 06:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('Na', 'N/A'), ('NEBULA', 'Nebula'), ('STAR', 'Star'), ('GALAXY', 'Galaxy'), ('PLANET', 'Planet')], default='Na', max_length=80)),
                ('photo', models.ImageField(null=True, upload_to='')),
                ('date', models.DateTimeField(default=datetime.datetime(2024, 2, 26, 3, 5, 46, 288726))),
                ('published', models.BooleanField(default=True)),
            ],
        ),
    ]
