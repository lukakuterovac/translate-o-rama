# Generated by Django 4.1.4 on 2023-02-04 20:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0014_job_translator_alter_job_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="job_field",
            field=models.CharField(
                choices=[
                    ("Art", "Art"),
                    ("Business", "Business"),
                    ("Computers", "Computers"),
                    ("Education", "Education"),
                    ("Engineering", "Engineering"),
                    ("Finance", "Finance"),
                    ("Law", "Law"),
                    ("Literature", "Literature"),
                    ("Medicine", "Medicine"),
                    ("Science", "Science"),
                    ("Social Sciences", "Social Sciences"),
                    ("Technology", "Technology"),
                ],
                default="Literature",
                max_length=15,
            ),
        ),
    ]