from django.contrib import admin

from . import models

class DeviceAdmin(admin.ModelAdmin):
  list_display = ('id','name', 'key', 'LINE_enable')
admin.site.register(models.Device, DeviceAdmin)
