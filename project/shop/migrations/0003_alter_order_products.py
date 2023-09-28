# Generated by Django 4.2.5 on 2023-09-20 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_orderproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='shop.OrderProduct', to='shop.product'),
        ),
    ]