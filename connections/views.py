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
