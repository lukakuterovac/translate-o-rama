# Generated by Django 4.1.4 on 2023-02-01 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_alter_job_options_message"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="budget",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]