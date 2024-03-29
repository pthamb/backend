# Generated by Django 5.0 on 2023-12-30 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0009_userprofile_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="childcare",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="coffeeTea",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="eldercare",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="errands",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="foodGathering",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="gardening",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="happyHours",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="movies",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="otherAdvice",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="petcare",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="repairAdvice",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="rides",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="running",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="shopping",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="swimming",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="televisionSports",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="tutoring",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="walking",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
