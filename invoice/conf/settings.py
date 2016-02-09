# -*- coding: UTF-8 -*-
from os import path
from django.conf import settings


INV_MODULE = getattr(settings, 'INV_MODULE', 'invoice.pdf')
INV_LOGO = getattr(settings, 'INV_LOGO', path.join('/var/www/ethernet/ethrnet/static/img/ethernet.png'))
FOOTER_LOGO = getattr(settings, 'FOOTER_LOGO', path.join('/var/www/ethernet/ethrnet/static/img/ethernet_footer.png'))
INV_CURRENCY = getattr(settings, 'INV_CURRENCY', u'EUR')
INV_CURRENCY_SYMBOL = getattr(settings, 'INV_CURRENCY_SYMBOL', u'€')
INV_EMAIL_SUBJECT = getattr(settings, 'INV_EMAIL_SUBJECT', u'[%s] Invoice %%(invoice_id)s' % (settings.SITE_NAME))
