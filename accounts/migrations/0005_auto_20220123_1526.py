# Generated by Django 2.2.12 on 2022-01-23 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_traders_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traders',
            name='Balance',
            field=models.BigIntegerField(),
        ),
    ]