# Generated by Django 4.2.5 on 2023-09-13 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='longitude',
        ),
    ]