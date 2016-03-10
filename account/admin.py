from django.contrib import admin
from account.models import UserAddress, UserProfile, Branch


admin.site.register(UserAddress)
admin.site.register(UserProfile)
admin.site.register(Branch)
