# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=35)),
                ('price', models.IntegerField()),
                ('published_on', models.DateTimeField(auto_now=True)),
                ('image', models.FileField(upload_to='C:\\Users\\agile\\shoppingsite\\fileuploads\\%Y\\%m\\%d')),
                ('image_1', models.FileField(upload_to='C:\\Users\\agile\\shoppingsite\\fileuploads\\%Y\\%m\\%d')),
                ('image_2', models.FileField(upload_to='C:\\Users\\agile\\shoppingsite\\fileuploads\\%Y\\%m\\%d')),
                ('ratings', models.CharField(choices=[('1', 'Worst'), ('2', 'Bed'), ('3', 'Average'), ('4', 'Good'), ('5', 'Best')], db_index=True, max_length=1, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('word', models.CharField(max_length=35)),
                ('slug', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='productdetails',
            name='Tags',
            field=models.ManyToManyField(to='shop.Tag', related_name='product_details'),
        ),
    ]
