from django.conf.urls import patterns, url
from dal import autocomplete
from inventory.models import IteamVariation

urlpatterns = patterns('',
                       url(r'^send/(?P<id>[0-9]+)/$', 'invoice.views.invoice_send', name='invoice_send'),
                       url(r'^get/(?P<id>[0-9]+)/$', 'invoice.views.get_invoice', name='get_invoice'),
                       url(r'^get/price/$', 'invoice.views.get_price', name='get_price'),
                       url(r'^pdf/(?P<pk>[0-9]+)/$', 'invoice.views.pdf_view', name='pdf_view'),
                       url(r'^create/$', 'invoice.views.create_invoice', name='create_invoice'),
                       url(r'^list/$', 'invoice.views.invoice_list', name='list_invoice'),
                       url(r'^variation/list/$',
                           'invoice.views.itemvarition_list',
                           name="list_itemvarition"),
                       url(r'^client/list/$',
                           'invoice.views.client_list',
                           name="list_client"),
                       )
