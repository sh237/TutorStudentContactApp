from django.contrib import admin
from .models import Calendar, Month, CalendarEvent
# Register your models here.
admin.site.register(Calendar)
# admin.site.register(models.Location)
admin.site.register(Month)
admin.site.register(CalendarEvent)