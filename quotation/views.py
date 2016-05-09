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
			HttpResponse('errors availabe on same page...goto the same page again.')

	else:
		user_form = QuotationForm()
		item_form = ItemForm()

	return render (request,'quotation/create.html',{'user_form':user_form, 'item_form':item_form})			

def itemlist(request):
	context = {}
	Quotation_list = Quotation.objects.all()
	
	context = {'Quotation_list':Quotation_list}
	return render(request,'quotation/view.html',context)

def detailitem(request,pk):
	context ={}
	quot = get_object_or_404(Quotation,pk=pk)
	item = Item.objects.all()
	context ={'quot':quot,'item':item}
	return render(request,'quotation/detail_item.html',context)