from django.conf.urls import patterns, url


urlpatterns = patterns('',
	url(r'^send/(?P<id>[0-9]+)/$', 'invoice.views.invoice_send', name='invoice_send'),
	url(r'^get/(?P<id>[0-9]+)/$', 'invoice.views.get_invoice', name='get_invoice'),
	url(r'^create/$', 'invoice.views.create_invoice', name='create_invoice'),
	url(r'^list/$', 'invoice.views.invoice_list', name='list_invoice'),
)
