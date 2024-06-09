# Generated by Django 5.0.3 on 2024-06-07 19:04

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("videos", "0011_alter_video_video_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="video_id",
            field=models.CharField(
                default=uuid.UUID("adcec58f-ef82-4414-990c-bccf31ffd300"),
                max_length=180,
            ),
        ),
    ]
