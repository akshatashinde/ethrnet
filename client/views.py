import json

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from account.models import UserAddress
from client.forms import ClientForm, AddressForm
from client.models import Client
from django.http import HttpResponse, HttpResponseRedirect

from fileupload.models import Picture


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
    print "client hit"
    clients = Client.objects.all().order_by('-id')[:5]
    client = []
    address = []
    address_id = request.POST.get('id_address')
    client_id = request.POST.get('id_client')
    if client_id:
        client = Client.objects.filter(id=client_id)
    if address_id:
        address = UserAddress.objects.filter(id=address_id)
    if request.method == "POST":
        client_form = ClientForm(request.POST)
        if client:
            client_form = ClientForm(request.POST, instance=client[0])
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
        if client:
            client_form = ClientForm(request.POST, instance=client[0])
        if address:
            address_form = AddressForm(request.POST, instance=address[0])

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
    address = []
    print "address hit"
    response = {}
    address_id = request.POST.get('id_address')
    if address_id:
        address = UserAddress.objects.filter(id=address_id)
    address_form = AddressForm(request.POST)
    if address:
            address_form = AddressForm(request.POST, instance=address[0])
    if address_form.is_valid():
        address = address_form.save()
        response['success'] = True
        response['address_id'] = address.id
        return HttpResponse(json.dumps(response))
    else:
        response['success'] = False
        return HttpResponse(json.dumps(response))


def client_address_images(request):
    client =[]
    address = []
    response = {}
    address_id = request.POST.get('id_address')
    client_id = request.POST.get('id_client')
    images_ids = request.POST.get('id_images')
    id_proof_types = request.POST.get('id_proof_types')
    address_proof_types = request.POST.get('address_proof_types')
    if address_id:
        address = UserAddress.objects.filter(id=address_id)
        if address:
            address = address[0]
    if client_id:
        client = Client.objects.filter(id=client_id)
        if client:
            client = client[0]
    if images_ids:
        images = Picture.objects.filter(id__in=images_ids.split(','))
    if address and client and images and id_proof_types and address_proof_types:
        client.Address = address
        client.attachments = images_ids.split(',')
        client.id_proof_types = id_proof_types
        client.address_proof_types = address_proof_types
        client.save()
        response['success'] = True
        response['url'] = reverse('dashboard')
    else:
        response['success'] = False
    return HttpResponse(json.dumps(response))


def client_update(request, id):
    pass


def client_delete(request, id):
    pass
