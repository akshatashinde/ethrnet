import json
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from plans.forms import ProductForm
from plans.models import Plans


def plan_list(request):
    print "plan_list"
    plans = Plans.objects.all()
    return render(
        request,
        'plans/plans_list.html',
        {
            'plans': plans,
            'page': 'plans'
        })


@login_required
def plan_create(request):
    print "plan_create"
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.created_by = request.user
            plan.updated_by = request.user
            plan.is_active = True
            plan.save()
            response = {}
            response['success'] = True
            response['id'] = plan.id
            response['plan_type'] = plan.plan_type
            response['price'] = plan.price
            response['is_active'] = plan.is_active
            response['download_speed'] = plan.download_speed
            response['FUP_limit'] = plan.FUP_limit
            response['installation_charges'] = plan.installation_charges
            response['subscription_amount'] = plan.subscription_amount
            return HttpResponse(json.dumps(response))
    else:
        form = ProductForm()
        plans = Plans.objects.all().order_by('-id')[:5]
    return render(
        request,
        'plans/plans_create.html',
        {
            'form': form,
            'plans': plans,
            'page': 'plans'
        })


def plan_update(request):
    print "plan_update"
    pass


def plan_delete(request):
    print "plan_delete"
    pass
