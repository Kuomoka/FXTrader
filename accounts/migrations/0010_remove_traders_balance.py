# Generated by Django 2.2.12 on 2022-01-23 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20220123_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traders',
            name='Balance',
        ),
    ]