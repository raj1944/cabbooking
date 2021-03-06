# Generated by Django 2.1.7 on 2019-04-12 04:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cabdriver',
            fields=[
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('otp', models.CharField(blank=True, max_length=100)),
                ('pickup', models.CharField(blank=True, max_length=100)),
                ('drop', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Current',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_uname', models.CharField(blank=True, max_length=100)),
                ('d_uname', models.CharField(blank=True, max_length=100)),
                ('pickup', models.CharField(blank=True, max_length=100)),
                ('drop', models.CharField(blank=True, max_length=100)),
                ('otp', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_uname', models.CharField(blank=True, max_length=100)),
                ('d_uname', models.CharField(blank=True, max_length=100)),
                ('pickup', models.CharField(blank=True, max_length=100)),
                ('drop', models.CharField(blank=True, max_length=100)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 12, 9, 30, 43, 617346))),
            ],
        ),
    ]
