from django.conf.urls import url
from connections import views



urlpatterns = [
    #url(r'^list/$', views.plan_list, name='plan_list'),
    url(r'^new/$', views.connection_create, name='connection_create'),
    url(r'^list/$', views.connection_list, name='connection_list'),
    #url(r'^edit/(?P<pk>[0-9]+)$', views.plan_update, name='plan_edit'),
    #url(r'^delete/(?P<pk>[0-9]+)$', views.plan_delete, name='plan_delete'),
]