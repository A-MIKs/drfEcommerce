# Generated by Django 3.2.8 on 2022-02-01 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0003_cart_session_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='session_id',
        ),
    ]
