# Generated by Django 4.0.2 on 2022-03-11 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_orders_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='delivered',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
