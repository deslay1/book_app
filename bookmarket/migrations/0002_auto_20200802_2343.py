# Generated by Django 3.0.8 on 2020-08-02 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('All', 'All')], default=('All', 'All'), max_length=50, verbose_name='What group do you want to publish to?'),
        ),
    ]
