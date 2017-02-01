from django.contrib import admin
from .models import Tag, ProductDetails

class TagAdmin(admin.ModelAdmin):
    #list_display = ('first_name', 'last_name')
    pass


class ProductDetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'published_on', 'ratings')
    list_filter = ('published_on', 'ratings')
    search_fields = ('name', 'price', 'Tags')

# Register your models here.
admin.site.register(Tag, TagAdmin)
admin.site.register(ProductDetails, ProductDetailsAdmin)
