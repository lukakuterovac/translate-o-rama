# Generated by Django 4.1.4 on 2023-02-04 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0011_alter_userprofile_is_translator"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="is_translator",
            field=models.BooleanField(null=True),
        ),
    ]
