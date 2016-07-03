from django.shortcuts import (render, HttpResponseRedirect,
                              redirect, get_object_or_404)
from django.core.urlresolvers import reverse
from account.forms import UserAddressForm, UserProfileForm
from account.models import UserAddress, UserProfile


def add_user_address(request):
    print request.GET
    try:
        next_page = request.GET.get("next")
    except:
        next_page = None
    form = UserAddressForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_address = form.save(commit=False)
            new_address.user = request.user
            new_address.save()
            return HttpResponseRedirect(reverse('sori-orders:address'))

    submit_btn = "Save Address"
    form_title = "Add New Address"
    return render(request, "account/form.html",
                  {"form": form,
                   "submit_btn": submit_btn,
                   "form_title": form_title,
                   })


def delete(request, pk):
    data = get_object_or_404(UserAddress, pk=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('sori-orders:address')
    return render(request, "account/confirm_delete.html", {'object': data})


def edit_profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES)
        user = UserProfile.objects.get(user=request.user)
        if form.is_valid():

            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.mobile_no = form.cleaned_data['mobile_no']
            user.gender = form.cleaned_data['gender']
            user.dob = form.cleaned_data['dob']
            user.profile_picture = form.cleaned_data['profile_picture']
            user.save()
            return redirect('sori-account:show_profile')
        else:
            form.errors
    else:
        form = UserProfileForm()
    return render(request, "account/profilepage.htm", {'form': form})


def show_profile(request):
    data = UserProfile.objects.filter(user=request.user)
    return render(request, "account/show_profile.html", {'data': data})

#############  admin site profile by amol #################


def admin_edit_profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES)
        user = UserProfile.objects.get(user=request.user)
        if form.is_valid():

            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.mobile_no = form.cleaned_data['mobile_no']
            user.gender = form.cleaned_data['gender']
            user.dob = form.cleaned_data['dob']
            user.profile_picture = form.cleaned_data['profile_picture']
            user.save()
            return redirect('sori-account:admin_show_profile')
        else:
            form.errors
    else:
        form = UserProfileForm()
    return render(request, "account/admin_profilepage.htm", {'form': form})


def admin_show_profile(request):
    data = UserProfile.objects.filter(user=request.user)
    return render(request, "account/admin_showprofile.html", {'data': data})
