# Generated by Django 5.0.4 on 2024-04-26 07:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='about')),
                ('status', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, default="Umumiy ma'lumotlar", null=True)),
            ],
            options={
                'verbose_name': "Umumiy ma'lumot",
                'verbose_name_plural': "Umumiy ma'lumotlari",
            },
        ),
        migrations.CreateModel(
            name='Corousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='carousel')),
                ('status', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('link', models.URLField(default='#')),
            ],
            options={
                'verbose_name': 'Corousel',
                'verbose_name_plural': "Corousel ma'lumotlari",
            },
        ),
        migrations.CreateModel(
            name='Qadamjo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('short_title', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='places')),
                ('status', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, default='Judayam chiroyli joylar', null=True)),
            ],
            options={
                'verbose_name': 'Qadamjo',
                'verbose_name_plural': "Qadamjo ma'lumotlari",
            },
        ),
        migrations.CreateModel(
            name='AboutImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about_us')),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.aboutus')),
            ],
            options={
                'verbose_name': 'rasm',
                'verbose_name_plural': 'Umumiy rasmlari',
            },
        ),
        migrations.CreateModel(
            name='FotoPlus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='places_photos')),
                ('pleace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.qadamjo')),
            ],
            options={
                'verbose_name': 'rasm',
                'verbose_name_plural': 'Qadamjo rasmlari',
            },
        ),
    ]
