from django.contrib import admin
from connections.models import Connection, ConnectionHistory


admin.site.register(Connection)
admin.site.register(ConnectionHistory)
