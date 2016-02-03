from django.conf.urls import url
from connections import views

urlpatterns = [
    url(r'^create/$', views.connection_create, name='connection_create'),
]