# Generated by Django 4.0.2 on 2022-03-09 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_suppliers_orders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suppliers',
            old_name='Username',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='suppliers',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='suppliers',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='suppliers',
            name='supplied',
        ),
        migrations.RemoveField(
            model_name='suppliers',
            name='supplies',
        ),
        migrations.RemoveField(
            model_name='suppliers',
            name='supply_date',
        ),
        migrations.AddField(
            model_name='suppliers',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='suppliers',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='suppliers',
            name='phone',
            field=models.BigIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Supplies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('cost', models.PositiveIntegerField()),
                ('supply_date', models.DateField()),
                ('supplied', models.BooleanField(default=False)),
                ('supplies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
            options={
                'verbose_name_plural': 'Supplies',
            },
        ),
    ]
