from django.conf.urls import include, url, patterns
from django.conf.urls import patterns

urlpatterns = patterns(
    '',
    url(r'^$', 'shop.views.index', name='index'),
    url(r'^create-payment$', 'shop.views.create_payment', name='create_payment'),
    url(r'^execute-payment', 'shop.views.execute_payment', name='execute_payment'),
)