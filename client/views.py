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
    if request.method == "POST":
        client_form = ClientForm(request.POST)
        address_form = AddressForm(request.POST)
        if client_form.is_valid() and address_form.is_valid():
            address = address_form.save(commit=False)
            address.save()
            client = client_form.save(commit=False)
            client.created_by = request.user
            client.Address = address
            client.save()

            response = {}
            response['success'] = True
            response['id'] = client.id
            response['name'] = client.name
            response['email'] = client.email
            response['phone_number'] = client.phone_number
            return HttpResponse(json.dumps(response))
    else:
        client_form = ClientForm()
        address_form = AddressForm()
        clients = Client.objects.all().order_by('-id')[:5]
    return render(
        request,
        'client/client_create.html',
        {
            'client_form': client_form,
            'address_form': address_form,
            'clients': clients,
            'page': 'client'
        })


def client_update(request, id):
    pass


def client_delete(request, id):
    pass