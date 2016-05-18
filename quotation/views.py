from django.shortcuts import render, get_object_or_404,get_object_or_404, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from .forms import QuotationForm,ItemForm
from django.contrib.auth.decorators import login_required
from .models import Quotation, Item
from django.forms import formset_factory
from client.models import Client
from django.contrib.auth.models import User
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
# Create your views here.
def home(request):
	return render(request, 'quotation/home.html',{})

@login_required(login_url='/admin/login/')
def createitem(request):
	if request.method == 'POST':
		user_form = QuotationForm(request.POST)
		item_form = ItemForm(request.POST)
		if user_form.is_valid() and item_form.is_valid():
			quotation_no = user_form.save()
			item = item_form.save(commit = False)
			item.quotation_no = quotation_no
			item.total = item.quantity * item.price
			item.save()
			messages.add_message(request, messages.INFO, 'user added details!')

			user_form = QuotationForm()
			item_form = ItemForm()
		else:
			messages.error(request,"Properly fill info....")
			return HttpResponseRedirect('')

	else:
		user_form = QuotationForm()
		item_form = ItemForm()

	return render (request,'quotation/create.html',{'user_form':user_form, 'item_form':item_form})		

@login_required(login_url='/admin/login/')
def itemlist(request):
	context = {}
	# clients = Client.objects.all(request.user)
	clients = Quotation.objects.all()
	context = {'clients':clients}
	return render(request,'quotation/view.html',context)

@login_required(login_url='/admin/login/')
# def detailitem(request,pk):
# 	context ={}
	
# 	client = get_object_or_404(Client, pk=pk, email=request.user)
# 	all_list = Item.objects.filter(client=client.client_id)
# 	print all_list
# 	context = {'client':client,
# 				'item':item,
# 				'all_list':all_list
# 			}
# 	return render(request,'quotation/bt.html',context)

def detailitem(request,pk):
	context ={}
	
	client = get_object_or_404(Quotation, pk=pk)
	all_list = Item.objects.filter(client=client.client)
	month = datetime.now() - timedelta(days = 30)
	last_month = Item.objects.filter(client=client.client,created__lt=month)
	print last_month
	months = datetime.month
	print months
	context = {'client':client,
				'all_list':all_list,
				'last_month':last_month,
				'months': months
			}
	return render(request,'quotation/bt.html',context)	

@login_required(login_url='/admin/login/')
def createitem_formset(request):
	ItemFormSet = formset_factory(ItemForm, extra=3, can_delete=True)
	if request.method == 'POST':
		user_form = QuotationForm(request.POST)
		formset = ItemFormSet(request.POST, request.FILES)
		if user_form.is_valid() and formset.is_valid() :
			quotation_no =  user_form.save(commit=False)
			quotation_no.save()
			clientid = request.POST.get('clientid')
			client = Client.objects.get(client_id=clientid)
			print client
			for form in formset:
			    item = form.save(commit=False)
			    item.quotation_no = quotation_no
			    item.client = client
			    item.total= item.quantity * item.price
			    item.save()

			messages.add_message(request, messages.INFO, 'user added details!')
			
			user_form = QuotationForm()
			formset = ItemFormSet()
		else:
			messages.error(request,"Properly fill information....entered another quotation no")
			return HttpResponseRedirect('')

	else:
		user_form = QuotationForm()
		formset = ItemFormSet()

	return render (request,'quotation/create1.html',{'user_form':user_form, 'formset':formset})			

@login_required(login_url='/admin/login/')
def tablelist(request):
	item_list = Item.objects.all()
	return render(request,'quotation/list.html', {'item_list': item_list})
