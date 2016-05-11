from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Table
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

try:
    from django.utils import importlib
except ImportError:
    import importlib

from invoice.conf import settings
from invoice.utils import format_currency


def draw_header(canvas):
    """ Draws the invoice header """

    canvas.drawInlineImage(settings.INV_LOGO, 0 * cm, -3.5 * cm, 600, 100)
    canvas.setFont('Helvetica', 20)
    canvas.drawString(9 * cm, -5 * cm, 'Invoice')


def draw_address(canvas):
    """ Draws the business address """
    pass


def draw_footer(canvas):
    """ Draws the invoice footer """
    note = (
        u'*Note: This is computer generated document',
    )
    textobject = canvas.beginText(1 * cm, -26 * cm)
    for line in note:
        textobject.textLine(line)
    canvas.drawText(textobject)
    canvas.drawInlineImage(settings.FOOTER_LOGO, 0 * cm, -30 * cm, 600, 90)


inv_module = importlib.import_module(settings.INV_MODULE)
header_func = inv_module.draw_header
address_func = inv_module.draw_address
footer_func = inv_module.draw_footer


def draw_pdf(buffer, invoice):
    """ Draws the invoice """
    canvas = Canvas(buffer, pagesize=A4)
    canvas.translate(0, 29.7 * cm)
    canvas.setFont('Helvetica', 10)

    canvas.saveState()
    header_func(canvas)
    canvas.restoreState()

    canvas.saveState()
    footer_func(canvas)
    canvas.restoreState()

    canvas.saveState()
    address_func(canvas)
    canvas.restoreState()

    # Client address
    textobject = canvas.beginText(1.5 * cm, -6.5 * cm)
    textobject.textLine('To,')
    textobject.textLine('Client ID : ' + invoice.user.client_id)
    textobject.textLine('Name : ' + invoice.user.name)
    if invoice.address.address:
        textobject.textLine('Address : ' + invoice.address.address)
    textobject.textLine(
        '                ' + invoice.address.flat_no + ',' + invoice.address.society + ',' + invoice.address.area)
    textobject.textLine('                ' + invoice.address.city + '- ' + invoice.address.zipcode)
    if invoice.address.country:
        textobject.textLine('                ' + invoice.address.state + ', ' + invoice.address.country)
    textobject.textLine('')
    textobject.textLine('Phone: +91-' + invoice.user.phone_number)
    textobject.textLine('Email: ' + invoice.user.email)
    canvas.drawText(textobject)

    # Info
    textobject = canvas.beginText(13 * cm, -6.5 * cm)
    textobject.textLine(u'Invoice ID: %s' % invoice.invoice_id)
    textobject.textLine(u'Invoice Date: %s' % invoice.invoice_date.strftime('%d %b %Y'))
    canvas.drawText(textobject)

    # Items
    data = [[u'Item', u'Quantity', u'Amount', u'Total'], ]
    invoice_list = invoice.items.all()
    for item in invoice.items.all():
        data.append([
            item.description,
            item.quantity,
            format_currency(item.unit_price, invoice.currency),
            format_currency(item.total(), invoice.currency)
        ])
    spaces_count = 25 - len(invoice_list)
    space_str = ""
    for i in range(0, spaces_count):
        space_str += '\n'
    data.append([space_str])
    data.append([u'', u'', u'Grand Total:', format_currency(invoice.total(), invoice.currency)])
    table = Table(data, colWidths=[11 * cm, 2 * cm, 3 * cm, 3 * cm])
    table.setStyle([
        ('FONT', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('TEXTCOLOR', (0, 0), (-1, -1), (0.2, 0.2, 0.2)),
        ('GRID', (0, 0), (-1, -2), 1, (0.7, 0.7, 0.7)),
        ('GRID', (-2, -1), (-1, -1), 1, (0.7, 0.7, 0.7)),
        ('ALIGN', (-2, 0), (-1, -1), 'RIGHT'),
        ('BACKGROUND', (0, 0), (-1, 0), (0.8, 0.8, 0.8)),
    ])
    tw, th, = table.wrapOn(canvas, 15 * cm, 19 * cm)
    table.drawOn(canvas, 1 * cm, -11 * cm - th)

    canvas.showPage()
    canvas.save()
