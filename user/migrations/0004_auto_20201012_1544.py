# Generated by Django 3.1.1 on 2020-10-12 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20201012_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_user',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='user_photos'),
        ),
    ]