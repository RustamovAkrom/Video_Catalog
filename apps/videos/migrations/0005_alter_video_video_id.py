# Generated by Django 5.0.3 on 2024-06-13 16:17

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_alter_video_video_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_id',
            field=models.CharField(default=uuid.UUID('730b313c-549c-41cc-bc4e-e796bff1b4fb'), max_length=180),
        ),
    ]
