from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .forms import ConnectForm
from .models import Connection


# Create your views here.
def connection_create(request):
    if request.method == "POST":
        form = ConnectForm(request.POST)
        connections = Connection.objects.all(request.user)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dashboard'))

    form = ConnectForm(request.POST)
    connections = Connection.objects.all(request.user)
    return render(
        request,
        'connection/connection_create.html',
        {
            'form': form,
            'connections': connections,
            'page': 'connections'
        })


def connection_list(request):
    connections = Connection.objects.all(request.user)
    return render(
        request,
        'connection/connection_list.html',
        {
            'connections': connections,
            'page': 'connections'
        })

def connection_update(request, id):
    connection = Connection.objects.filter(id=id)
    if connection:
        connection = connection[0]
        if request.POST:
            form = ConnectForm(request.POST, instance=connection)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('connections:connection_list'))

        form = ConnectForm(instance=connection)
        connections = Connection.objects.all(request.user).order_by('-id')[:5]

        return render(
            request,
            'connection/connection_create.html',
            {
                'form': form,
                'connections': connections,
                'page': 'connections',
                'edit': True
            })

def connection_delete(request, id):
    connection = Connection.objects.filter(id=id)
    connection.delete()
    return HttpResponseRedirect(reverse('connections:connection_list'))        