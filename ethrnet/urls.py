"""ethrnet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #
    url(r'^connections/', include('connections.urls', namespace='connections')),
    # url(r'^enquiries/', include('enquiries.urls', namespace='enquiries')),
    # url(r'^plans/', include('plans.urls', namespace='plans')),
    # url(r'^reports/', include('reports.urls', namespace='reports')),
    # url(r'^advertisements/', include('advertisements.urls', namespace='advertisements')),
    url(r'$^', 'core.views.client'),
    url(r'^myadmin/$', login_required(TemplateView.as_view(template_name="admin_base.html"))),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/login/'}, name='logout'),
    url(r'^plan/', include('plans.urls', namespace='ethernet-plans')),
    url(r'^invoice/', include('invoice.urls', namespace='ethernet-invoice')),
    url(r'^client/', include('client.urls', namespace='ethernet-client')),
]
