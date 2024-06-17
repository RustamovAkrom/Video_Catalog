# Generated by Django 5.0.3 on 2024-06-17 02:55

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofile_email_userprofile_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(default=uuid.UUID('065e143e-18c1-4464-9b3a-b9f6a7229b26'), max_length=128),
        ),
        migrations.DeleteModel(
            name='UserUrls',
        ),
    ]