# Generated by Django 4.2.6 on 2023-10-19 20:19

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_rename_donation_donation_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 10, 19, 20, 19, 30, 825896, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
