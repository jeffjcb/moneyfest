# Generated by Django 3.1.7 on 2021-03-30 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20210302_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email_preference',
            field=models.BooleanField(default=True),
        ),
    ]
