# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160503_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nick',
            field=models.CharField(unique=True, max_length=24),
        ),
    ]
