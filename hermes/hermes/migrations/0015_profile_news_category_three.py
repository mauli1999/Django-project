# Generated by Django 4.1.3 on 2022-11-14 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hermes', '0014_profile_news_category_two'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='news_category_three',
            field=models.CharField(choices=[('Technology', 'Technology'), ('Business', 'Business'), ('Sports', 'Sports')], default='Technology', max_length=20),
        ),
    ]
