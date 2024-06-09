# Generated by Django 5.0.3 on 2024-06-02 12:33

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("videos", "0007_rename_vodeo_video_video_alter_video_video_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="description",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="video",
            name="video_id",
            field=models.CharField(
                default=uuid.UUID("937a153a-93a5-43c5-b94b-b7d01def68ef"),
                max_length=180,
            ),
        ),
    ]
