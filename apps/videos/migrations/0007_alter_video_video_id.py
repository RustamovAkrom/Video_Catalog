# Generated by Django 5.0.3 on 2024-06-17 02:55

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_alter_video_video_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_id',
            field=models.CharField(default=uuid.UUID('b7bbf925-b76e-4ae2-b1b4-f72e782be0b3'), max_length=180),
        ),
    ]
