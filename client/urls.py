from django.conf.urls import url
from client import views


urlpatterns = [
    url(r'^list/$', views.client_list, name='client_list'),
    url(r'^new$', views.client_create, name='client_create'),
    url(r'^address/new$', views.create_address, name='create_address'),
    url(r'^edit/(?P<id>[0-9]+)$', views.client_update, name='client_update'),
    url(r'^delete/(?P<id>[0-9]+)$', views.client_delete, name='client_delete'),
]
