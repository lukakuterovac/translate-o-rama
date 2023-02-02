# Generated by Django 4.1.4 on 2023-02-02 10:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0007_merge_0004_alter_job_options_0006_alter_job_budget"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="is_assigned",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="job",
            name="is_completed",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="job",
            name="title",
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name="message",
            name="send_date",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
