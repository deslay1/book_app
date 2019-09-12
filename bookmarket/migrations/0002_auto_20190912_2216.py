# Generated by Django 2.1.3 on 2019-09-12 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='SellerOrBuyer',
            field=models.CharField(choices=[('Buyer', 'Buy'), ('Seller', 'Sell')], default=('Buyer', 'Buy'), max_length=50, verbose_name='Are you here to buy or sell?'),
        ),
    ]
