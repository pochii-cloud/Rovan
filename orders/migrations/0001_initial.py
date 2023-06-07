# Generated by Django 4.0.2 on 2022-03-09 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0004_remove_orders_product_delete_suppliers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('cost', models.PositiveIntegerField()),
                ('date_ordered', models.DateField(auto_now=True)),
                ('delivered', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
            options={
                'verbose_name_plural': 'orders',
            },
        ),
    ]