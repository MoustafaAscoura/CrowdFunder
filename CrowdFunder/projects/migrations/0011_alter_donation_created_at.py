# Generated by Django 4.2.6 on 2023-10-20 21:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_alter_donation_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='created_at',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 10, 20, 21, 22, 40, 289346, tzinfo=datetime.timezone.utc)),
        ),
    ]