# Generated by Django 4.0.2 on 2022-03-11 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplies', '0004_alter_supplies_supplied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplies',
            name='supplied',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
