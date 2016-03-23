from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^add/item/$', 'inventory.views.item_add', name='add_item'),
    url(r'^item/(?P<id>[0-9]+)/$', 'inventory.views.item_edit', name='edit_item'),
    url(r'^item/delete/(?P<id>[0-9]+)/$', 'inventory.views.item_delete', name='delete_item'),
    url(r'^list/item/$', 'inventory.views.item_list', name='list_item'),
    url(r'^add/item/(?P<id>[0-9]+)/inventory$', 'inventory.views.inventory_item_add', name='add_item_inventory'),
    url(r'^item/inventory/edit/(?P<id>[0-9]+)$', 'inventory.views.inventory_item_edit', name='edit_item_inventory'),
    url(r'^item/inventory/delete/(?P<id>[0-9]+)$', 'inventory.views.inventory_item_delete', name='delete_item_inventory'),
)
