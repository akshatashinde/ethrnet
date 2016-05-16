from django.conf.urls import url
from plans import views



urlpatterns = [
    url(r'^list/$', views.plan_list, name='plan_list'),
    url(r'^new$', views.plan_create, name='plan_new'),
    url(r'^edit/(?P<id>[0-9]+)/$', views.plan_update, name='plan_edit'),
    url(r'^get/$', views.get_plan, name='plan_get'),
    url(r'^get/list/$', views.get_plan_list, name='get_plan_list'),
    url(r'^delete/(?P<id>[0-9]+)/$', views.plan_delete, name='plan_delete'),
]