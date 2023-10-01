# Generated by Django 4.2.4 on 2023-08-25 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0007_remove_customer_username'),
        ('storeapp', '0016_remove_cart_completed_remove_cart_owner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UserProfile.customer'),
        ),
        migrations.AddField(
            model_name='cart',
            name='session_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]