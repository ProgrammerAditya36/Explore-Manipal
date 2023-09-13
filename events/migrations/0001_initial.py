# Generated by Django 4.2.5 on 2023-09-13 10:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_Events',
            fields=[
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('time', models.TimeField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
