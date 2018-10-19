from django.contrib import admin

from .models import DetailRegistration


@admin.register(DetailRegistration)
class DetailRegistrationAdmin(admin.ModelAdmin):
    pass
