# Generated by Django 5.1.6 on 2025-03-27 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0003_notes_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="notes",
            name="public",
            field=models.BooleanField(default=False),
        ),
    ]
