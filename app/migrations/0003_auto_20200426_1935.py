# Generated by Django 3.0.5 on 2020-04-26 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_clients_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
