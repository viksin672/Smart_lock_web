# Generated by Django 3.0.5 on 2020-04-26 14:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200426_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='entry',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
