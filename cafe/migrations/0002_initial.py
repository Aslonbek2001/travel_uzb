# Generated by Django 5.0.4 on 2024-04-26 07:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cafe', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='cafe',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chayxana', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cafeimages',
            name='chayxana',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fotos', to='cafe.cafe'),
        ),
        migrations.AddField(
            model_name='foods',
            name='cafe',
            field=models.ForeignKey(help_text='choyxona', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='cafe.cafe'),
        ),
    ]
