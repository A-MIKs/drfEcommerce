# Generated by Django 4.0.5 on 2022-07-04 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0013_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='img'),
        ),
    ]
