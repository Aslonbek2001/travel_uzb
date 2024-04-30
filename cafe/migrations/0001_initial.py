# Generated by Django 5.0.4 on 2024-04-26 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, default='Nomi', max_length=100)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('info', models.TextField(blank=True, help_text="Umumiy ma'lumotlar kiritish kerak", null=True)),
                ('image', models.ImageField(blank=True, default=None, help_text='Choyxona rasimi', null=True, upload_to='restaurant')),
                ('status', models.BooleanField(default=False)),
                ('phone', models.CharField(blank=True, max_length=9, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Cafe',
                'verbose_name_plural': 'Cafelar',
            },
        ),
        migrations.CreateModel(
            name='CafeImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default=None, help_text='Choyxona rasimi', null=True, upload_to='chayxana_images')),
            ],
            options={
                'verbose_name': 'Chayxana rasmi',
                'verbose_name_plural': 'Chayxana rasmlari',
            },
        ),
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, default='Nomi', max_length=100)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(choices=[('drink', 'drink'), ('food', 'food'), ('dessert', 'dessert')], default='food', max_length=100)),
                ('image', models.ImageField(blank=True, default=None, help_text='menu', null=True, upload_to='menu_item')),
                ('description', models.TextField(blank=True, help_text="Umumiy ma'lumotlar", null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Chayxana minusi',
                'verbose_name_plural': 'Chayxona minulari',
                'ordering': ['id'],
            },
        ),
    ]
