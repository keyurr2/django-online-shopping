import os
from django.db import models
from django.utils.translation import ugettext_noop
from django.conf import settings
# Create your models here.


class Tag(models.Model):
    """
    Author : Keyur Rathod
    Use : store tags
    """
    word        = models.CharField(max_length=35)
    slug        = models.CharField(max_length=250)
    created_at  = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.word

    def __str__(self):
        return self.word

class ProductDetails(models.Model):
    """
    Author : Keyur Rathod
    Use : store Product Details
    """
    name = models.CharField(max_length=35, blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    published_on = models.DateTimeField(auto_now=True)
    image = models.FileField(upload_to='fileuploads\%Y\%m\%d', blank=False, null=False)
    image_1 = models.FileField(upload_to='fileuploads\%Y\%m\%d', blank=True, null=True)
    image_2 = models.FileField(upload_to='fileuploads\%Y\%m\%d', blank=True, null=True)
    RATING_CHOICE = (
        ('1', ugettext_noop('Worst')),
        ('2', ugettext_noop('Bed')),
        ('3', ugettext_noop('Average')),
        ('4', ugettext_noop('Good')),
        ('5', ugettext_noop('Best')),
    )
    ratings = models.CharField(
        blank=True, null=True, max_length=1, db_index=True, choices=RATING_CHOICE
    )
    Tags = models.ManyToManyField(Tag,related_name='product_details', blank=False, null=False)


    def __str__(self):
        return self.name