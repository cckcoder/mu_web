# Generated by Django 4.1.6 on 2023-02-09 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='feature_image',
            field=models.ImageField(blank=True, null=True, upload_to='feature_images'),
        ),
    ]