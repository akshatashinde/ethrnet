from django.conf.urls import url
from reports import views



urlpatterns = [
    url(r'^client/$', views.client_reports, name='client_reports'),
    url(r'^inventory/$', views.inventory_reports, name='inventory_reports'),
    url(r'^piechart/$', views.piechart, name='piechart'),
    url(r'^barchart/$', views.barchart, name='barchart'),
    url(r'^client_list/$',views.client_list, name ='client_list'),
    url(r'^connection_detail/(?P<pk>[0-9]+)/$',views.connecntion_detail, name ='connection_detail'),
    url(r'^sheet/$',views.upload, name ='upload'),
    url(r'^sheet1/$',views.generate_book_csv, name ='generate_book_csv'),
    url(r'^(?P<pk>[0-9]+)/$',views.generate_book_excel, name ='generate_book_excel'),
]