# Generated by Django 2.2.5 on 2020-07-16 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(default='default.jpg', upload_to='post_pics', verbose_name='Image ')),
                ('image2', models.ImageField(blank=True, upload_to='post_pics', verbose_name='Additional image 1 (optional) ')),
                ('image3', models.ImageField(blank=True, upload_to='post_pics', verbose_name='Additional image 2 (optional) ')),
                ('price', models.DecimalField(decimal_places=2, default='0.0', max_digits=6)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('SellerOrBuyer', models.CharField(choices=[('Buyer', 'Buy'), ('Seller', 'Sell')], default=('Buyer', 'Buy'), max_length=50, verbose_name='Are you here to buy or sell? ')),
                ('Condition', models.CharField(blank=True, choices=[('', 'Please choose if possible'), ('As New', 'As New'), ('Very Good', 'Very Good'), ('Acceptable', 'Acceptable'), ('Mixed', 'Mixed')], max_length=50, verbose_name='Condition of book(s) <small> <br /> If you have multiple books of varying conditions, choose "mixed" </small>')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='post_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
                ('comuser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='bookmarket.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
                ('comuser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='bookmarket.Post')),
            ],
        ),
    ]
