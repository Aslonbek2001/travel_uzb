# Generated by Django 5.0.4 on 2024-04-30 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]