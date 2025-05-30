# Generated by Django 5.2.1 on 2025-05-24 19:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beauty_zone', '0004_alter_service_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='service',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(seconds=1800)),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='services/'),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
