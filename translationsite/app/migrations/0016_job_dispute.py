# Generated by Django 4.1.4 on 2023-02-04 11:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0015_merge_20230204_1108"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="dispute",
            field=models.TextField(blank=True, null=True),
        ),
    ]
