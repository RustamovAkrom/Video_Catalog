# Generated by Django 5.0.3 on 2024-06-04 17:57

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(default=uuid.UUID('ce7b93b4-d236-4080-8ce1-90d34d55713c'), max_length=128),
        ),
    ]
