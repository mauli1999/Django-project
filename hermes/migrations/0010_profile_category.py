# Generated by Django 4.1.2 on 2022-11-07 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hermes', '0009_profile_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='category',
            field=models.CharField(default='Top News', max_length=20),
        ),
    ]