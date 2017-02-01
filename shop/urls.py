from django.conf.urls import include, url, patterns
from django.conf.urls import patterns

urlpatterns = patterns(
    '',
    url(r'^$', 'shop.views.index', name='index'),
)