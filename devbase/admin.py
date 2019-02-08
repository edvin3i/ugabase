from django.contrib import admin
from devbase.models import Organization, Building, AutomationSystem, Device, Events

admin.site.register(Organization)
admin.site.register(Building)
admin.site.register(AutomationSystem)
admin.site.register(Device)
admin.site.register(Events)
