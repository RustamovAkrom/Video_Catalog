# Generated by Django 5.0.3 on 2024-06-08 16:18

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0008_alter_user_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="user_id",
            field=models.CharField(
                default=uuid.UUID("01324742-b13a-4be5-a6e3-85f35040a61f"),
                max_length=128,
            ),
        ),
    ]
