# Generated by Django 5.0 on 2023-12-10 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("person", models.CharField(max_length=200)),
                ("age", models.IntegerField()),
                ("email", models.CharField(max_length=200)),
                ("address", models.IntegerField()),
                ("mobile", models.CharField(max_length=120, unique=True)),
                ("walking", models.CharField(max_length=200)),
                ("running", models.CharField(max_length=200)),
                ("gardening", models.CharField(max_length=200, null=True)),
                ("swim", models.CharField(max_length=200)),
                ("tea", models.CharField(max_length=200, null=True)),
                ("like", models.CharField(max_length=200, null=True)),
                ("tv", models.CharField(max_length=200, null=True)),
                ("movie", models.CharField(max_length=200, null=True)),
                ("shopping", models.CharField(max_length=200, null=True)),
                ("happy", models.CharField(max_length=200, null=True)),
                ("erands", models.CharField(max_length=200, null=True)),
                ("rides", models.CharField(max_length=200, null=True)),
                ("childcare", models.CharField(max_length=200, null=True)),
                ("eldercare", models.CharField(max_length=200, null=True)),
                ("petcare", models.CharField(max_length=200, null=True)),
                ("tutoring", models.CharField(max_length=200, null=True)),
                ("home", models.CharField(max_length=200, null=True)),
                ("landscape", models.CharField(max_length=200, null=True)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("sharePreference", models.CharField(max_length=200)),
            ],
        ),
    ]
