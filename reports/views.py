import csv
import xlwt
import json

from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
from django.template import RequestContext
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, HttpResponse, render_to_response
from django.db.models import Count
from django.shortcuts import render, HttpResponse, render_to_response, get_object_or_404, HttpResponseRedirect


from .forms import UploadFileForm
from client.models import Client
from connections.models import Connection, ConnectionHistory
from client.models import Client
from connections.models import Connection
from inventory.models import InventoryItem, IteamVariation
from plans.models import Plans

def client_reports(request):
    clients = Client.objects.all(request.user)
    return render(request, 'reports/report.html', {'clients':clients})

def inventory_reports(request):
    context = {}
    inventory_item = InventoryItem.objects.all(request.user)
    context = {'inventory_item':inventory_item}
    return render(request,'reports/inventory_item.html',context)

def inventory_detail(request,pk):
    inventory_item = InventoryItem.objects.filter(pk=pk)
    itm =IteamVariation.objects.filter(inventoryitem = inventory_item)
    month = datetime.now() - timedelta(days = 30)
    last_month = IteamVariation.objects.filter(inventoryitem = inventory_item,purchased_at__lt=month)
    sdate = None
    ldate = None
    custom = None
    mnth = None
    year=None
    l_month=None
    if request.is_ajax():
        if request.method == "POST" and request.POST['action'] == 'start1':
            print 3
            sdate = request.POST.get('start_date')
            ldate = request.POST.get('last_date')
           
            request.session['sdate']=sdate
            request.session['ldate']=ldate
            custom = IteamVariation.objects.filter(inventoryitem = inventory_item,purchased_at__range=(sdate,ldate))
            print custom
            data = serializers.serialize("json", custom)
            return HttpResponse(data, content_type='application/json')

        if request.method == "POST" and request.POST['action'] == 'start2':
            year = request.POST.get('currentdate')
            request.session['year']=year
            yearwise = IteamVariation.objects.filter(inventoryitem = inventory_item,purchased_at__year = year)
            year_data = serializers.serialize("json", yearwise)
            return HttpResponse(year_data, content_type='application/json')
        
        if request.method == "POST" and request.POST['action'] == 'start3':
            mnth = request.POST.get('idfname')
            request.session['mnth']=mnth
            monthwise = IteamVariation.objects.filter(inventoryitem = inventory_item,purchased_at__month = mnth)
            month_data = serializers.serialize("json", monthwise)
            return HttpResponse(month_data, content_type='application/json')

        if request.method == "POST" and request.POST['action'] == 'start4':
            l_month = request.POST.get('action')
            print l_month
            request.session['l_month']=l_month
            month = datetime.now() - timedelta(days = 30)
            last_month = IteamVariation.objects.filter(inventoryitem = inventory_item,purchased_at__lt=month)
            last_month_data = serializers.serialize("json", last_month)
            return HttpResponse(last_month_data, content_type='application/json')
                        
    return render(
        request,
        'reports/inventory_details.html',
        {
            'inventory_item': inventory_item,
            'itm': itm,
            'last_month':last_month,
        })

def generate_item_excel(request,pk):
        
        
        inventory_item = InventoryItem.objects.filter(pk=pk)
        
        sdate=request.session['sdate']
        ldate=request.session['ldate']
        year=request.session['year']
        mnth=request.session['mnth']
        l_month=request.session['l_month']
        l_month1='start4'

        print sdate,ldate

        if year is None:
            year = 0

        
        items = IteamVariation.objects.filter(inventoryitem = inventory_item)
        
        if mnth != 0:
            items = IteamVariation.objects.filter(inventoryitem = inventory_item,purchased_at__month = mnth)
            print items,1
        elif year != 0:
            items = IteamVariation.objects.filter(inventoryitem = inventory_item,purchased_at__year = year)
            print items,2    
        elif sdate and ldate is not None:
            items = IteamVariation.objects.filter(inventoryitem = inventory_item,purchased_at__range=(sdate,ldate))
            print items,3
        elif l_month == l_month1:
            month = datetime.now() - timedelta(days = 30)
            items = IteamVariation.objects.filter(inventoryitem = inventory_item,purchased_at__lt=month)
            print items,4
        else:
            items = IteamVariation.objects.filter(inventoryitem = inventory_item)
            print items,5

        objectlist = []
        for conn in items:
            object = {}
            object['code'] = conn.code
            object['status'] = conn.status
            object['quantity'] = conn.quantity
            object['price'] = conn.price
            object['sale_price'] = conn.sale_price
            object['purchased_at'] = conn.purchased_at



            # client = Client.objects.get(client_id= conn.client)
            # object['client'] = client.name
            # object['client_id'] = client.client_id
            # plan =Plans.objects.get(code = conn.plan)
            # object['plan'] = plan.code
            objectlist.append(object)
               

        # Create the HttpResponse object with Excel header.This tells browsers that 
        # the document is a Excel file.
        response = HttpResponse(content_type='application/ms-excel')

        # The response also has additional Content-Disposition header, which contains 
        # the name of the Excel file.
        response['Content-Disposition'] = 'attachment; filename=Inventory_details.xls'

        # Create object for the Workbook which is under xlwt library.
        workbook = xlwt.Workbook()

        # By using Workbook object, add the sheet with the name of your choice.
        worksheet = workbook.add_sheet("Inventory Report")
     
        row_num = 0
        columns = ['Item_Code','Status','Quantity','Price','Sale_price','purchased_at']
        for col_num in range(len(columns)):
            # For each cell in your Excel Sheet, call write function by passing row number, 
            # column number and cell data.
            worksheet.write(row_num, col_num, columns[col_num])     
       
        for item in objectlist:
            row_num += 1
            row = [item['code'],item['status'],item['quantity'],item['price'],item['sale_price'],item['purchased_at']]
            for col_num in range(len(row)):
                worksheet.write(row_num, col_num, row[col_num])
       
        workbook.save(response)
     
        request.session['sdate'] = 0
        request.session['ldate']= 0
        request.session['year'] = 0
        request.session['mnth'] = 0
        request.session['l_month'] = None
        return response


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
    mnth = None
    if request.is_ajax():
        if request.method == "POST" and request.POST['action'] == 'start1':
            print 3
            sdate = request.POST.get('start_date')
            ldate = request.POST.get('last_date')
           
            request.session['sdate']=sdate
            request.session['ldate']=ldate
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
            request.session['year']=year
            yearwise = ConnectionHistory.objects.filter(client = clients,created_on__year = year)
            year_data = serializers.serialize("json", yearwise)
            return HttpResponse(year_data, content_type='application/json')

        if request.method == "POST" and request.POST['action'] == 'start3':
            print 5
            mnth = request.POST.get('idfname')
            request.session['mnth']=mnth
            print mnth
            monthwise = ConnectionHistory.objects.filter(client = clients,created_on__month = mnth)
            print monthwise
            month_data = serializers.serialize("json", monthwise)
            return HttpResponse(month_data, content_type='application/json')
        if request.method == "POST" and request.POST['action'] == 'start4':
            l_month = request.POST.get('action')
            print l_month
            request.session['l_month']=l_month
            month = datetime.now() - timedelta(days = 30)
            last_month = ConnectionHistory.objects.filter(client=clients,created_on__lt=month)
            last_month_data = serializers.serialize("json", last_month)
            return HttpResponse(last_month_data, content_type='application/json')            
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

def generate_book_excel(request,pk):
        
        
        clients = Client.objects.filter(pk=pk)
        
        sdate=request.session['sdate']
        ldate=request.session['ldate']
        year=request.session['year']
        mnth=request.session['mnth']
        l_month=request.session['l_month']
        l_month1='start4'

        if year is None:
            year = 0

        print sdate,ldate
        print year
        print mnth
        print l_month
        books = ConnectionHistory.objects.filter(client=clients)
        
        if mnth != 0:
            books = ConnectionHistory.objects.filter(client = clients,created_on__month = mnth)
            print books,1
        elif year != 0:
            books = ConnectionHistory.objects.filter(client = clients,created_on__year = year)
            print books,2    
        elif sdate and ldate is not None:
            books = ConnectionHistory.objects.filter(client = clients,created_on__range=(sdate,ldate))
            print books,3
        elif l_month == l_month1:
            month = datetime.now() - timedelta(days = 30)
            books = ConnectionHistory.objects.filter(client=clients,created_on__lt=month)
            print books,4
        else:
            books = ConnectionHistory.objects.filter(client=clients)
            print books,5

        objectlist = []
        for conn in books:
            object = {}
            object['created_on'] = conn.created_on
            object['expired_on'] = conn.expired_on

            client = Client.objects.get(client_id= conn.client)
            object['client'] = client.name
            object['client_id'] = client.client_id
            plan =Plans.objects.get(code = conn.plan)
            object['plan'] = plan.code
            objectlist.append(object)
               

        # Create the HttpResponse object with Excel header.This tells browsers that 
        # the document is a Excel file.
        response = HttpResponse(content_type='application/ms-excel')

        # The response also has additional Content-Disposition header, which contains 
        # the name of the Excel file.
        response['Content-Disposition'] = 'attachment; filename=Connection_History.xls'

        # Create object for the Workbook which is under xlwt library.
        workbook = xlwt.Workbook()

        # By using Workbook object, add the sheet with the name of your choice.
        worksheet = workbook.add_sheet("Connection History Report")
     
        row_num = 0
        columns = ['Client_id','Client_Name','Plan','Created_on','Expired_on']
        for col_num in range(len(columns)):
            # For each cell in your Excel Sheet, call write function by passing row number, 
            # column number and cell data.
            worksheet.write(row_num, col_num, columns[col_num])     
       
        for book in objectlist:
            row_num += 1
            row = [book['client_id'],book['client'],book['plan'],book['created_on'],book['expired_on']]
            for col_num in range(len(row)):
                worksheet.write(row_num, col_num, row[col_num])
       
        workbook.save(response)
     
        request.session['sdate'] = 0
        request.session['ldate']= 0
        request.session['year'] = 0
        request.session['mnth'] = 0
        request.session['l_month'] = None
        return response
