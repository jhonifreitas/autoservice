# Generated by Django 2.2.10 on 2020-06-02 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20200602_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='time',
            field=models.CharField(default='', max_length=255, verbose_name='Horário'),
            preserve_default=False,
        ),
    ]
