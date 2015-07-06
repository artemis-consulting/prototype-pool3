# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinformation',
            name='contact_name',
            field=models.CharField(default='name', max_length=100),
            preserve_default=False,
        ),
    ]