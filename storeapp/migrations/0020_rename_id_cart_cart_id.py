# Generated by Django 4.2.4 on 2023-08-25 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0019_alter_cartitems_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='id',
            new_name='cart_id',
        ),
    ]
