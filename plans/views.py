import json

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from account.models import Branch
from plans.forms import ProductForm
from plans.models import Plans
from django.views.decorators.http import require_http_methods
from django.core import serializers


def plan_list(request):
    print "plan_list"
    plans = Plans.objects.all(request.user)
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
        plans = Plans.objects.all(request.user).order_by('-id')[:5]
    return render(
        request,
        'plans/plans_create.html',
        {
            'form': form,
            'plans': plans,
            'page': 'plans',
            'edit': False
        })


def plan_update(request, id):
    plan = Plans.objects.filter(id=id)
    if plan:
        plan = plan[0]
        if request.POST:
            form = ProductForm(request.POST, instance=plan)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('ethernet-plans:plan_list'))

        form = ProductForm(instance=plan)
        plans = Plans.objects.all(request.user).order_by('-id')[:5]

        return render(
            request,
            'plans/plans_create.html',
            {
                'form': form,
                'plans': plans,
                'page': 'plans',
                'edit': True
            })

def plan_delete(request, id):
    plan = Plans.objects.filter(id=id)
    plan.delete()
    return HttpResponseRedirect(reverse('ethernet-plans:plan_list'))



@require_http_methods(["GET", "POST"])
def get_plan(request):
    if request.is_ajax():
        id = request.POST.get('id')

        data = serializers.serialize("json", Plans.objects.filter(id=id))

    else:
        data = 'Not valid request'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


@require_http_methods(["GET", "POST"])
def get_plan_list(request):
    mimetype = 'application/json'
    result= {}
    if request.is_ajax():
        data = request.POST
        if data.get('area'):
            branch = Branch.objects.filter(id=data.get('area'))
            if branch:
                branch = branch[0]

            plans = Plans.objects.filter(branch=branch)
            for plan in plans:
                result[plan.id] = plan.code
    data = json.dumps(result)
    return HttpResponse(data, mimetype)
