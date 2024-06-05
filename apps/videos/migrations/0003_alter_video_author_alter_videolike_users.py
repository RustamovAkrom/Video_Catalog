# Generated by Django 5.0.3 on 2024-06-02 08:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile'),
        ('videos', '0002_video_author_video_category_video_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_author', to='users.userprofile'),
        ),
        migrations.AlterField(
            model_name='videolike',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='video_likes', to='users.userprofile'),
        ),
    ]
