from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from plans.models import Plans


def client(request):
    plans = Plans.objects.all()
    return render(
        request,
        'base.html',
        {'plans': plans}
    )