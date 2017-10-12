# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-07 22:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('hash', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now=True, verbose_name='Created at')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('original_file', models.FileField(upload_to='./static/uploads', verbose_name='File')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
        ),
        migrations.CreateModel(
            name='PictureFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='', verbose_name='File')),
                ('picture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='museum.Picture', verbose_name='Picture')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('method', models.CharField(choices=[('CRP', 'Crop'), ('CVR', 'Cover'), ('CNT', 'Contain'), ('HGT', 'Height'), ('WDT', 'Width'), ('TMB', 'Thumbnail')], default='WDT', max_length=3, verbose_name='Method')),
                ('height', models.IntegerField(default=0, verbose_name='Height')),
                ('width', models.IntegerField(default=0, verbose_name='Width')),
            ],
        ),
        migrations.AddField(
            model_name='picturefile',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='museum.Size', verbose_name='Size'),
        ),
    ]
