# Generated by Django 5.0.4 on 2024-04-30 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_driver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverydrivers',
            name='is_avaliable',
            field=models.BooleanField(default=True),
        ),
    ]
