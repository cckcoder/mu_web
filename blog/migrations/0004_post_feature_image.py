# Generated by Django 4.1.6 on 2023-02-10 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='feature_image',
            field=models.ImageField(blank=True, null=True, upload_to='feature_image'),
        ),
    ]
