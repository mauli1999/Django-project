# Generated by Django 4.1.2 on 2022-10-29 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hermes', '0008_remove_profile_country_remove_profile_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(default='No Country', max_length=20),
        ),
    ]
