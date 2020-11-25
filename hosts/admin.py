from django.contrib import admin

from . models import Host, Vlan

admin.site.register(Host)
admin.site.register(Vlan)