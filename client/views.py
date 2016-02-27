import json
from django.shortcuts import render
from client.forms import ClientForm, AddressForm
from client.models import Client
from django.http import HttpResponse


def client_list(request):
    clients = Client.objects.all()
    return render(
        request,
        'client/client_list.html',
        {
            'clients': clients,
            'page': 'client'
        })


def client_create(request):
    clients = Client.objects.all().order_by('-id')[:5]
    if request.method == "POST":
        client_form = ClientForm(request.POST)
        address_form = AddressForm(request.POST)
        if client_form.is_valid():
            client = client_form.save(commit=False)
            client.created_by = request.user
            client.save()

            response = {}
            response['success'] = True
            response['client_id'] = client.id
            return HttpResponse(json.dumps(response))
        else:
            return render(
                request,
                'client/client_create.html',
                {
                    'client_form': client_form,
                    'address_form': address_form,
                    'clients': clients,
                    'page': 'client'
                })
    else:
        client_form = ClientForm()
        address_form = AddressForm()
    return render(
        request,
        'client/client_create.html',
        {
            'client_form': client_form,
            'address_form': address_form,
            'clients': clients,
            'page': 'client'
        })

def create_address(request):
    response = {}
    address_form = AddressForm(request.POST)
    if address_form.is_valid():
        address = address_form.save()
        response['success'] = True
        response['address_id'] = address.id
        return HttpResponse(json.dumps(response))
    else:
        response['success'] = False
        return HttpResponse(json.dumps(response))

def client_update(request, id):
    pass


def client_delete(request, id):
    pass
