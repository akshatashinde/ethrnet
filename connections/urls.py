from django.conf.urls import url
from connections import views


urlpatterns = [
    #url(r'^list/$', views.plan_list, name='plan_list'),
    url(r'^new/$', views.connection_create, name='connection_create'),
    url(r'^list/$', views.connection_list, name='connection_list'),
    url(r'^edit/(?P<id>[0-9]+)$',
        views.connection_update, name='connection_edit'),
    url(r'^delete/(?P<id>[0-9]+)$',
        views.connection_delete, name='connection_delete'),

]
