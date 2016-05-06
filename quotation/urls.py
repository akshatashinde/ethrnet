from django.conf.urls import include, url
from django.contrib import admin
from quotation import views

app_name='quotation'
urlpatterns = [
	url(r'^$',views.home, name='home'),
	]