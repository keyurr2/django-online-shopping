# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20160312_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='image',
            field=models.FileField(upload_to='C:\\Users\\agile\\staticfiles/media_cfileuploads\\%Y\\%m\\%d'),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='image_1',
            field=models.FileField(upload_to='C:\\Users\\agile\\staticfiles/media_cfileuploads\\%Y\\%m\\%d', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='image_2',
            field=models.FileField(upload_to='C:\\Users\\agile\\staticfiles/media_cfileuploads\\%Y\\%m\\%d', null=True, blank=True),
        ),
    ]
