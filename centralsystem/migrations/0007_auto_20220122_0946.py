# Generated by Django 2.2.12 on 2022-01-22 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centralsystem', '0006_balances_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemusers',
            name='Balance',
            field=models.IntegerField(),
        ),
    ]