# Generated by Django 5.0 on 2024-01-08 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0015_userprofile_errands"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="errands",
        ),
    ]
