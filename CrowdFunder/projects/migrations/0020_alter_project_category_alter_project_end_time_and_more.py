# Generated by Django 4.2.6 on 2023-10-23 11:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_alter_project_total_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_time',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_time',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
