from django.contrib import admin
from account.models import UserAddress, UserProfile


admin.site.register(UserAddress)
admin.site.register(UserProfile)
