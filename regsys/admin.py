from django.contrib import admin

from .models import DetailRegistration, Payment


@admin.register(DetailRegistration)
class DetailRegistrationAdmin(admin.ModelAdmin):
    pass


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass
