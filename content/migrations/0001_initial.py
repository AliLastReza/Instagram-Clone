# Generated by Django 2.2 on 2020-03-20 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='modified time ')),
                ('caption', models.TextField(blank=True, verbose_name='caption')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='location.Location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='modified time ')),
                ('title', models.CharField(max_length=32, verbose_name='title')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TagegedUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='modified time ')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_post', to='content.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='modified time ')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hashtags', to='content.Post')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='content.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='modified time ')),
                ('media_types', models.PositiveSmallIntegerField(choices=[(1, 'Image'), (2, 'Video')], default=1, verbose_name='media types')),
                ('media_file', models.FileField(upload_to='content/media/', verbose_name='media files')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='content.Post')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
