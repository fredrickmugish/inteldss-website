# Generated by Django 5.0 on 2024-04-10 07:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0004_team"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="team",
            options={"verbose_name": "team", "verbose_name_plural": "team"},
        ),
        migrations.AlterField(
            model_name="team",
            name="image",
            field=models.ImageField(upload_to="images"),
        ),
    ]
