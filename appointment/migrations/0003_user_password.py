# Generated by Django 5.1 on 2024-09-28 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_alter_user_medical_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='null', max_length=8),
        ),
    ]
