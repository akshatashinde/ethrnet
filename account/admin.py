from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext as _

from account.models import UserProfile
from django.contrib.auth.models import User
from account.models import UserAddress 
from soriuser.models import SORIUser
from .forms import PPIUserCreationForm, PPIUserChangeForm


class UserInline(admin.StackedInline):
    """
    This class displays UserProfile inline with User.
    """
    model = UserProfile
    can_delete = False

class UserAdmin(UserAdmin):

    form = PPIUserChangeForm
    add_form = PPIUserCreationForm

    list_display = ('email', 'is_active')
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('personal info', {
            'fields': ('date_joined',)
        }),
        ('permissions', {'fields': ('is_active', 'is_staff')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',),
                'fields': ('email', 'password', 'password_repeat')}),)
    search_fields = ('email',)
    ordering = ('email',)
    readonly_fields = ('date_joined',)
    filter_horizontal = ()
    inlines = (UserInline,)


class AdminSite(AdminSite):
    site_title = _('SOPI site')
    site_header = _('SOPI administration')
    index_title = _('SOPI Site administration')

class UserAddressAdmin(admin.ModelAdmin):
    class Meta:
        model = UserAddress


admin.site = AdminSite()
admin.site.register(User, UserAdmin)
admin.site.register(UserAddress, UserAddressAdmin)

