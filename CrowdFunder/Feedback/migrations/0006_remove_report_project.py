# Generated by Django 4.2.6 on 2023-10-27 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Feedback', '0005_rename_cotent_comment_content_report_comment_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='project',
        ),
    ]
