# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20160312_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='image',
            field=models.FileField(upload_to='fileuploads\\%Y\\%m\\%d'),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='image_1',
            field=models.FileField(upload_to='fileuploads\\%Y\\%m\\%d', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='image_2',
            field=models.FileField(upload_to='fileuploads\\%Y\\%m\\%d', blank=True, null=True),
        ),
    ]
