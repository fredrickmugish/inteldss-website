# Generated by Django 5.0 on 2024-04-10 04:45

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Organization",
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
                ("name", models.CharField(max_length=200)),
                ("location", models.CharField(max_length=200)),
                ("type", models.CharField(max_length=200)),
            ],
        ),
    ]
