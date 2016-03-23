from django.conf.urls import patterns, url
from account.views import add_user_address, show_profile, edit_profile, admin_edit_profile,admin_show_profile

urlpatterns = patterns('',
	url(r'^ajax/add_user_address/$', 'account.views.add_user_address', name='ajax_add_user_address'),
	url(r'^account/address/add/$', 'account.views.add_user_address', name='add_user_address'),
	url(r'^delete/(?P<pk>[0-9]+)/$', 'account.views.delete', name='delete'),

	url(r'^profile/$',show_profile, name='show_profile'),
    url(r'^profile/edit/$',edit_profile, name='edit_profile'),

    url(r'^adminprofile/$',admin_show_profile, name='admin_show_profile'),
    url(r'^adminprofile/edit/$',admin_edit_profile, name='admin_edit_profile'),
)