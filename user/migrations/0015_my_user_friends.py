# Generated by Django 3.1.1 on 2020-11-20 12:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0014_my_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_user',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='friends', to=settings.AUTH_USER_MODEL),
        ),
    ]