# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 00:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=200)),
                ('free_time', models.FloatField(blank=True, default=0.0, null=True)),
                ('stop_charges', models.FloatField(blank=True, default=0.0, null=True)),
                ('exam_stop', models.FloatField(blank=True, default=0.0, null=True)),
                ('fuel_surcharge', models.FloatField(blank=True, default=0.0, null=True)),
                ('storage_dry', models.FloatField(blank=True, default=0.0, null=True)),
                ('storage_cold', models.FloatField(blank=True, default=0.0, null=True)),
                ('drayage', models.FloatField(blank=True, default=0.0, null=True)),
                ('contact_fname', models.CharField(default='', max_length=40, null=True)),
                ('contact_lname', models.CharField(default='', max_length=60, null=True)),
                ('street_address', models.CharField(max_length=200, null=True)),
                ('state', models.CharField(max_length=40, null=True)),
                ('zipcode', models.CharField(max_length=30, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Zips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zipcode', models.CharField(blank=True, max_length=30, null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='subcompany',
            name='zip_service',
            field=models.ManyToManyField(to='adminPortal.Zips'),
        ),
    ]
