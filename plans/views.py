from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from plans.forms import ProductForm


def plan_list(request):
    print "plan_list"
    return render(request, 'plans/plans_list.html', {})
    pass

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
            return HttpResponse('Success')
        else:
            pass
    else:
        form = ProductForm()
    return render(request, 'plans/plans_create.html', {'form': form,})
    pass


def plan_view(request):
    print "plan_view"
    pass


def plan_update(request):
    print "plan_update"
    pass


def plan_delete(request):
    print "plan_delete"
    pass
