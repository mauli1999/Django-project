# Generated by Django 4.1.2 on 2022-10-29 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hermes', '0003_rename_user_first_name_profile_first_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='first_name',
            new_name='f_name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='last_name',
            new_name='l_name',
        ),
    ]