# Generated by Django 5.0 on 2024-04-10 05:39

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0002_disruptor_alter_organization_options"),
    ]

    operations = [
        migrations.RenameField(
            model_name="disruptor",
            old_name="name",
            new_name="affected_aspect",
        ),
    ]
