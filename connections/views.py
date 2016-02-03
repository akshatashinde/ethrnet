from django.shortcuts import render
from connections.models import Connection
from connections.forms import ConnectionForm

def connection_create(request):
    print "connection_create"
    if request.method == "POST":
        form = ConnectionForm(request.POST)
        if form.is_valid():
            connection = form.save(commit=False)
            connection.is_active = True
            connection.save()
            # response = {}
            # response['success'] = True
            # response['id'] = plan.id
            # response['plan_type'] = plan.plan_type
            # response['price'] = plan.price
            # response['is_active'] = plan.is_active
            # response['download_speed'] = plan.download_speed
            # response['FUP_limit'] = plan.FUP_limit
            # response['installation_charges'] = plan.installation_charges
            # response['subscription_amount'] = plan.subscription_amount
            # return HttpResponse(json.dumps(response))
    else:
        form = ConnectionForm()
    return render(
        request,
        'connections/create_connection.html',
        {
            'form': form,
        })

