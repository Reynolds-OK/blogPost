# Generated by Django 3.1.5 on 2021-08-11 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210810_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='articles',
        ),
    ]
