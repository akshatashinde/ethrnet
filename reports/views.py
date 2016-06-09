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
    clients = Client.objects.filter(pk=pk)
    conn =Connection.objects.filter(client = clients)
    all_list = ConnectionHistory.objects.filter(client=clients)
    month = datetime.now() - timedelta(days = 30)
    last_month = ConnectionHistory.objects.filter(client=clients,created_on__lt=month)
    sdate = None
    ldate = None
    custom = None
    if request.is_ajax():
        if request.method == "POST" and request.POST['action'] == 'start1':
            print 3
            sdate = request.POST.get('start_date')
            ldate = request.POST.get('last_date')
            print sdate,ldate
            custom = ConnectionHistory.objects.filter(client = clients,created_on__range=(sdate,ldate))
            print custom
            data = serializers.serialize("json", custom)
            return HttpResponse(data, content_type='application/json')
            # to_json = []
            # for cust in custom:
            #     dog_dict = {}
            #     dog_dict['id'] = cust.client
            #     dog_dict['plan'] = cust.plan
            #     dog_dict['status'] = cust.is_active
            #     dog_dict['created'] = cust.created_on
            #     dog_dict['expired'] = cust.expired_on
            #     to_json.append(dog_dict)
            # print to_json
            # # response_data =json.dumps(to_json)
            # response_data=serializers.serialize("json", to_json)
            # return HttpResponse(response_data,mimetype_type='application/json')    
        
        if request.method == "POST" and request.POST['action'] == 'start2':
            year = request.POST.get('currentdate')
            yearwise = ConnectionHistory.objects.filter(client = clients,created_on__year = year)
            year_data = serializers.serialize("json", yearwise)
            return HttpResponse(year_data, content_type='application/json')

        if request.method == "POST" and request.POST['action'] == 'start3':
            print 5
            mnth = request.POST.get('idfname')
            print mnth
            monthwise = ConnectionHistory.objects.filter(client = clients,created_on__month = mnth)
            print monthwise
            month_data = serializers.serialize("json", monthwise)
            return HttpResponse(month_data, content_type='application/json')        
    print 6
   
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

