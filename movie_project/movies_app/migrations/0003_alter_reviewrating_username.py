# Generated by Django 4.2.7 on 2024-02-26 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0002_reviewrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewrating',
            name='username',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]