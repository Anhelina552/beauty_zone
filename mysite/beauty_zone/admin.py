from django.contrib import admin
from .models import Service, Master, Appointment
from .models import GalleryImage

admin.site.register(GalleryImage)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration_str')
    search_fields = ('name',)

@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'service', 'master', 'appointment_datetime')
    list_filter = ('service', 'master', 'appointment_datetime')
    search_fields = ('client_name', 'client_phone')
