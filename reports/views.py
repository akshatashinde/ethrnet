from django.shortcuts import render, HttpResponse, render_to_response, get_object_or_404, HttpResponseRedirect
from client.models import Client
from plans.models import Plans
from connections.models import Connection, ConnectionHistory
from django.db.models import Count
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
from .forms import UploadFileForm
from django.template import RequestContext
import csv
import xlwt
from .models import Book
import json
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def client_reports(request):
    clients = Client.objects.all(request.user)
    return render(request, 'reports/report.html', {})


def inventory_reports(request):
    return HttpResponse('<h2>Inventory Reports</h2>')


def piechart(request):
    from nvd3 import pieChart
    chart = pieChart(name='pieChart', color_category='category20c',
                     height=400, width=350)
    all_clients = Client.objects.all(request.user).values('id', 'is_active')
    xdata = ["Acitve User", "Inavive User"]
    ydata = [all_clients.filter(is_active=True).count(), all_clients.filter(is_active=False).count()]

    extra_serie = {"tooltip": {"y_start": "", "y_end": " user"}}
    chart.add_serie(y=ydata, x=xdata, extra=extra_serie)
    chart.buildhtml()
    context = {}
    context['html_data'] = chart.htmlcontent
    return render(request, 'reports/piechart.html', context)


def barchart(request):
    from nvd3 import multiBarChart
    # conn = Connection.objects.filter(created_on__year='2016').extra({'month' : "MONTH(created_on)"}).values_list('month').annotate(total_item=Count('id'))
    chart2 = multiBarChart(width=400, height=350, x_axis_format=None)
    xdata = ['Jan', 'Feb', 'March', 'Apr', 'May', 'June']
    ydata1 = [6, 12, 9, 16, 22, 21]
    ydata2 = [8, 14, 7, 11, 10, 14]
    context = {}
    chart2.add_serie(name="New Connection", y=ydata1, x=xdata)
    chart2.add_serie(name="Inventory Out", y=ydata2, x=xdata)
    chart2.buildhtml()
    context['html_data2'] = chart2.htmlcontent
    return render(request, 'reports/barchart.html', context)

def client_list(request):
    context = {}
    clients = Client.objects.all(request.user)
    context = {'clients':clients}
    return render(request,'reports/client_view.html',context)    




def connecntion_detail(request,pk):
    mimetype = 'application/json'
    clients = Client.objects.filter(pk=pk)
    conn =Connection.objects.filter(client = clients)
    all_list = ConnectionHistory.objects.filter(client=clients)
    month = datetime.now() - timedelta(days = 30)
    last_month = ConnectionHistory.objects.filter(client=clients,created_on__lt=month)
    sdate = None
    ldate = None
    custom = None
    if request.is_ajax():
        if request.method == "POST":
            print 3
            sdate = request.POST.get('start_date')
            ldate = request.POST.get('last_date')
            print sdate,ldate
            custom = ConnectionHistory.objects.filter(client = clients,created_on__range=(sdate,ldate))
            print custom
            data = serializers.serialize("json", custom)
            return HttpResponse(data, content_type='application/json')
            # result = {}
            # pickup_records=[]

            # for cust in custom:
            #         client = cust.client
            #         plan = cust.plan
            #         is_active = cust.is_active
            #         created_on = cust.created_on
            #         expired_on = cust.expired_on
            #         record = {"id":client, "rplan":plan, "status":is_active,"created_on":created_on,"expired_on":expired_on}
            #         print record
            #         pickup_records.append(record)

            # result["data"] = pickup_records   
            # rec = {"Boolean": true,"Null": null,"Number": 123} 
            # pickup_records.append(rec)
            # return HttpResponse(pickup_records)
            # return HttpResponse(json.dumps(pickup_records),mimetype)
        
    print 4
   
    return render(
        request,
        'reports/connection_detail.html',
        {
            'clients': clients,
            'page': 'client',
            'conn':conn,
            'all_list':all_list,
            'last_month':last_month,
        })

