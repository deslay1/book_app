# Generated by Django 2.2.13 on 2020-07-25 10:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookmarket', '0002_auto_20200724_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='approved_comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='comment_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='comment_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=300, verbose_name='Enter below:'),
        ),
    ]
