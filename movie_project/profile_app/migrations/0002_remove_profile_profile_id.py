# Generated by Django 4.2.7 on 2024-02-26 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_id',
        ),
    ]
