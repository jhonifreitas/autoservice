# Generated by Django 2.2.10 on 2020-06-03 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_service_text_cancel'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='lat',
            field=models.CharField(default='', max_length=255, verbose_name='Latitude'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='lng',
            field=models.CharField(default='', max_length=255, verbose_name='Longitude'),
            preserve_default=False,
        ),
    ]
