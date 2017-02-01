# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20160312_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='image_1',
            field=models.FileField(null=True, blank=True, upload_to='C:\\Users\\agile\\shoppingsite\\fileuploads\\%Y\\%m\\%d'),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='image_2',
            field=models.FileField(null=True, blank=True, upload_to='C:\\Users\\agile\\shoppingsite\\fileuploads\\%Y\\%m\\%d'),
        ),
    ]
