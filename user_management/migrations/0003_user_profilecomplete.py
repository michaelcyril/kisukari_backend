# Generated by Django 5.0.3 on 2024-04-02 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_alter_user_height_alter_user_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profileComplete',
            field=models.BooleanField(default=False),
        ),
    ]
