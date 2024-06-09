# Generated by Django 5.0.3 on 2024-06-09 08:50

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("videos", "0018_alter_video_video_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="video_id",
            field=models.CharField(
                default=uuid.UUID("de51a496-3a70-4a0f-9e47-b36a9eb4e86c"),
                max_length=180,
            ),
        ),
    ]