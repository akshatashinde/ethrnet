import StringIO
import xlsxwriter
 
def WriteToExcel(weather_data, town=None):
    output = StringIO.StringIO()
    workbook = xlsxwriter.Workbook(output)
 
    # Here we will adding the code to add data
 
    workbook.close()
    xlsx_data = output.getvalue()
    # xlsx_data contains the Excel file
    return xlsx_data