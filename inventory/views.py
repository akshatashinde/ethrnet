from django.shortcuts import render, get_object_or_404
from inventory.forms import ItemForm, IteamVariationForm
from inventory.models import *
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def item_add(request):
    itemform = ItemForm(request.POST)
    if request.method == "POST":
        if itemform.is_valid():
            item = itemform.save(commit=False)
            item.branch = request.user.userprofile.branch
            item.save()
            itemform = ItemForm()
    inventoryitems = InventoryItem.objects.all(request.user)
    return render(
        request,
        'inventory/item_create.html',
        {
            'itemform': itemform,
            'inventoryitems': inventoryitems,
            'page': 'inventory'
        })


def item_edit(request, id):
    item = InventoryItem.objects.filter(id=id)
    if item:
        item = item[0]
        itemform = ItemForm(instance=item)
        if request.method == "POST":
            itemform = ItemForm(request.POST, instance=item)
            if itemform.is_valid():
                itemform.save()
                return HttpResponseRedirect(reverse('ethernet-inventory:add_item'))
        inventoryitems = InventoryItem.objects.all(request.user)
        return render(
            request,
            'inventory/item_create.html',
            {
                'itemform': itemform,
                'inventoryitems': inventoryitems,
                'page': 'inventory'
            })


def item_delete(request, id):
    item = InventoryItem.objects.filter(id=id)
    item.delete()
    return HttpResponseRedirect(reverse('ethernet-inventory:add_item'))


def item_list(request):
    pass


def inventory_item_add(request, id):
    item = InventoryItem.objects.filter(id=id)
    if item:
        item = item[0]
        form = IteamVariationForm(request.POST)
        if request.method == "POST":
            if form.is_valid():
                itemvariation = form.save(commit=False)
                itemvariation.inventoryitem = item
                itemvariation.branch = request.user.userprofile.branch
                itemvariation.save()
                form = IteamVariationForm()
        inventoryitems = IteamVariation.objects.filter(inventoryitem=id,branch=request.user.userprofile.branch)
        if request.user.is_staff:
            inventoryitems = IteamVariation.objects.filter(inventoryitem=id)
        return render(
            request,
            'inventory/variation_create.html',
            {
                'form': form,
                'inventoryitems': inventoryitems,
                'page': 'inventory'
            })
    return HttpResponseRedirect(reverse('ethernet-inventory:add_item'))


def inventory_item_edit(request, id):
    item = IteamVariation.objects.filter(id=id)
    if item:
        item = item[0]
        form = IteamVariationForm(instance=item)
        if request.method == "POST":
            form = IteamVariationForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(
                    reverse('ethernet-inventory:add_item_inventory',
                            args=(item.inventoryitem.id,)
                            )
                )
        inventoryitems = IteamVariation.objects.all(request.user)
        return render(
            request,
            'inventory/variation_create.html',
            {
                'form': form,
                'inventoryitems': inventoryitems,
                'page': 'inventory'
            })
    return HttpResponseRedirect(reverse('ethernet-inventory:add_item'))


def inventory_item_delete(request, id):
    item = IteamVariation.objects.filter(id=id)
    if item:
        item = item[0]
        ids = item.inventoryitem.id
        item.delete()
        return HttpResponseRedirect(
            reverse('ethernet-inventory:add_item_inventory',
                    args=(ids,)
                    )
        )
    return HttpResponseRedirect(reverse('ethernet-inventory:add_item'))
