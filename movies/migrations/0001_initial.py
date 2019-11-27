# Generated by Django 2.2.5 on 2019-11-27 02:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('open_date', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('audi_score', models.IntegerField()),
                ('net_score', models.IntegerField()),
                ('press_score', models.IntegerField()),
                ('audi', models.IntegerField()),
                ('rate', models.CharField(max_length=20)),
                ('naver_code', models.CharField(max_length=20)),
                ('poster', models.TextField()),
                ('youtube_score', models.FloatField()),
                ('genre', models.ManyToManyField(related_name='genre_movies', to='movies.Genre')),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_movies', to=settings.AUTH_USER_MODEL)),
                ('watched_user', models.ManyToManyField(blank=True, related_name='watched_movie', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-youtube_score',),
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channelId', models.CharField(max_length=50)),
                ('channelTitle', models.CharField(max_length=100)),
                ('videoTitle', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('videoId', models.CharField(max_length=50)),
                ('created_at', models.CharField(max_length=100)),
                ('thumbnail_small', models.CharField(max_length=200)),
                ('thumbnail_medium', models.CharField(max_length=200)),
                ('thumbnail_high', models.CharField(max_length=200)),
                ('view_count', models.IntegerField()),
                ('like_count', models.IntegerField()),
                ('dislike_count', models.IntegerField()),
                ('comment_count', models.IntegerField()),
                ('video_src', models.CharField(max_length=200)),
                ('iframe', models.TextField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_reviews', to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='Movie_Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]