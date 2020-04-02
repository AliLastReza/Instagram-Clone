# Generated by Django 2.2 on 2020-03-23 05:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmedia',
            name='media_file',
            field=models.FileField(upload_to='content/media/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('jpg', 'jpeg', 'mpd'))], verbose_name='media files'),
        ),
    ]
