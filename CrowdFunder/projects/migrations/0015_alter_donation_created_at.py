# Generated by Django 4.2.6 on 2023-10-21 16:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_alter_donation_created_at_alter_project_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 10, 21, 16, 3, 39, 888139, tzinfo=datetime.timezone.utc)),
        ),
    ]
