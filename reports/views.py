from django.shortcuts import render, HttpResponse, render_to_response, get_object_or_404
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
    sdate = request.POST.get('s_date')
    ldate = request.POST.get('l_date')
    mnth = request.POST.get('fname')
    print mnth
    year= request.POST.get('currentDate')
    print year
    custom = ConnectionHistory.objects.filter(client = clients,created_on__range=(sdate,ldate))
    if mnth is None:
        monthwise = 0
        pass
    else :
        monthwise = ConnectionHistory.objects.filter(client = clients,created_on__month = mnth)
        print monthwise


    if year is None:
        yearwise = 0
        pass
    else:
        yearwise = ConnectionHistory.objects.filter(client = clients,created_on__year = year)
        print yearwise
       
    request.session['sdate']=sdate
    request.session['ldate']=ldate 
    request.session['mnth'] = mnth 
    request.session['year'] = year     
    return render(
        request,
        'reports/connection_detail.html',
        {
            'clients': clients,
            'page': 'client',
            'conn':conn,
            'all_list':all_list,
            'last_month':last_month,
            'custom':custom,
            'monthwise':monthwise,
            'yearwise':yearwise
        }) 

# def excelreport(request):
#     # if request.method == 'POST':
#     if 'excel' in request.POST:
#         response = HttpResponse(content_type='application/vnd.ms-excel')
#         response['Content-Disposition'] = 'attachment; filename=Report.xlsx'
#         xlsx_data = WriteToExcel(weather_period, town)
#         response.write(xlsx_data)
#     return response
    
# def WriteToExcel(weather_data, town=None):
#     import StringIO
#     import xlsxwriter
#     output = StringIO.StringIO()
#     workbook = xlsxwriter.Workbook(output)
#     worksheet_s = workbook.add_worksheet("Summary")
#     title = workbook.add_format({
#         'bold': True,
#         'font_size': 14,
#         'align': 'center',
#         'valign': 'vcenter'
#     })
#     header = workbook.add_format({
#         'bg_color': '#F7F7F7',
#         'color': 'black',
#         'align': 'center',
#         'valign': 'top',
#         'border': 1
# })
#     # Here we will adding the code to add data
 
#     workbook.close()
#     xlsx_data = output.getvalue()
#     # xlsx_data contains the Excel file
#     return xlsx_data    
#     

def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            return excel.make_response(filehandle.get_sheet(), "csv", file_name="download")
    else:
        form = UploadFileForm()
    return render_to_response('reports/upload_form.html', {'form': form}, context_instance=RequestContext(request))

def generate_book_csv(request):
        books = Book.objects.all()

        # Create the HttpResponse object with CSV header.This tells browsers that 
        # the document is a CSV file.
        response = HttpResponse(content_type='text/csv')

        # The response also has additional Content-Disposition header, which contains 
        # the name of the CSV file.
        response['Content-Disposition'] = 'attachment; filename=books.csv'

        # The csv.writer function takes file-like object as argument i.e.,HttpResponse object
        writer = csv.writer(response)

        # For each row in your CSV file, call writer.writerow function by passing 
        # a list or tuple to it.
        writer.writerow(['ID', 'Title', 'Description'])

        for book in books:
            writer.writerow([book.id, book.title, book.description])
        return response  

def generate_book_excel(request,pk):
        
        clients = Client.objects.filter(pk=pk)
        # books = ConnectionHistory.objects.filter(client=clients)
        sdate=request.session['sdate']
        ldate=request.session['ldate']
        mnth = request.session['mnth']
        year = request.session['year']
        print mnth

        if sdate and ldate is not None:
            books = ConnectionHistory.objects.filter(client = clients,created_on__range=(sdate,ldate))

        # elif mnth is not None:
        #     try:
        #         books = ConnectionHistory.objects.filter(client = clients,created_on__month = mnth)  
        #     except ConnectionHistory.DoesNotExist:
        #         books = None
        else:
            books = ConnectionHistory.objects.filter(client=clients)   
            

        objectlist = []
        for conn in books:
            object = {}
            object['created_on'] = conn.created_on
            object['expired_on'] = conn.expired_on

            client = Client.objects.get(id = books)
            # client = get_object_or_404(Client,client = clients)
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
        return response
