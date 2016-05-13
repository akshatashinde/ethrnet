from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from .forms import QuotationForm,ItemForm
from django.contrib.auth.decorators import login_required
from .models import Quotation, Item
from django.forms import formset_factory

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
	Quotation_list = Quotation.objects.all()
	
	context = {'Quotation_list':Quotation_list}
	return render(request,'quotation/view.html',context)

@login_required(login_url='/admin/login/')
def detailitem(request,pk):
	context ={}
	quot = get_object_or_404(Quotation,pk=pk)
	item = Item.objects.all()
	context ={'quot':quot,'item':item}
	return render(request,'quotation/detail_item.html',context)

@login_required(login_url='/admin/login/')
def createitem_formset(request):
	ItemFormSet = formset_factory(ItemForm, extra=3, can_delete=True)
	print 1
	if request.method == 'POST':
		print 'a'
		user_form = QuotationForm(request.POST)
		print 'a1'
		formset = ItemFormSet(request.POST, request.FILES)
		print 2
		if user_form.is_valid() and formset.is_valid() :
			print 3
			quotation_no =  user_form.save(commit=False)
			print quotation_no	
			quotation_no.save()
			print 4
			for form in formset:
			    item = form.save(commit=False)
			    item.quotation_no = quotation_no
			    item.total= item.quantity * item.price
			    item.save()
			    print item.item

			messages.add_message(request, messages.INFO, 'user added details!')
			
			user_form = QuotationForm()
			formset = ItemFormSet()
		else:
			messages.error(request,"Properly fill information....")
			return HttpResponseRedirect('')

	else:
		user_form = QuotationForm()
		formset = ItemFormSet()

	return render (request,'quotation/create1.html',{'user_form':user_form, 'formset':formset})			

@login_required(login_url='/admin/login/')
def tablelist(request):
	item_list = Item.objects.all()
	return render(request,'quotation/list.html', {'item_list': item_list})
