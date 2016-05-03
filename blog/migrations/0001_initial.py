# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=32)),
                ('content', models.TextField(max_length=2000)),
                ('create_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nick', models.CharField(max_length=24)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=32)),
                ('type', models.IntegerField(max_length=4)),
                ('create_time', models.DateTimeField()),
                ('modify_time', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(related_name='author', to='blog.User'),
        ),
    ]
