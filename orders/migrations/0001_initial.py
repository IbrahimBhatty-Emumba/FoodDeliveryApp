# Generated by Django 5.0.4 on 2024-05-03 15:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('delivery_driver', '0002_alter_deliverydrivers_is_avaliable'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdersItemsM2M',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('is_completed', models.BooleanField(auto_created=True, default=False)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('delivery_driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery_driver.deliverydrivers')),
            ],
        ),
    ]
