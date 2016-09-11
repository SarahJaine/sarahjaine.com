# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-08 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sarahjaine', '0004_auto_20160908_1501'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='project',
            name='git_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='hosted_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, to='sarahjaine.Tag'),
        ),
    ]